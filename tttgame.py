import pygame
import sys
import time

# Initialize pygame
pygame.init()

# === Game Constants ===
WIDTH, HEIGHT = 600, 700
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE
LINE_WIDTH = 15
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 12
CROSS_WIDTH = 20
SPACE = SQUARE_SIZE // 4
TURN_TIME_LIMIT = 10  # seconds

# === Color Theme ===
BG_COLOR = (240, 248, 255)
LINE_COLOR = (70, 130, 180)
CIRCLE_COLOR = (0, 102, 204)
CROSS_COLOR = (220, 20, 60)
TEXT_COLOR = (50, 50, 50)

BUTTON_COLOR = (30, 144, 255)
BUTTON_HOVER_COLOR = (0, 191, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
WIN_LINE_COLOR = (34, 139, 34)  # Green for win line

# === Setup ===
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# === Game State ===
board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
player = 'X'
game_over = False
winner = None
win_coords = None
score = {'X': 0, 'O': 0}
turn_start_time = time.time()


def draw_lines():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)


def draw_win_line(start_pos, end_pos):
    pygame.draw.line(screen, WIN_LINE_COLOR, start_pos, end_pos, LINE_WIDTH)


def check_win():
    global win_coords
    for row in range(BOARD_SIZE):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0]:
            win_coords = ((0, row), (2, row))
            return board[row][0]
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]:
            win_coords = ((col, 0), (col, 2))
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        win_coords = ((0, 0), (2, 2))
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        win_coords = ((2, 0), (0, 2))
        return board[0][2]
    return None


def is_board_full():
    return all(board[row][col] is not None for row in range(BOARD_SIZE) for col in range(BOARD_SIZE))


def draw_status():
    pygame.draw.rect(screen, BG_COLOR, (0, WIDTH, WIDTH, HEIGHT - WIDTH))
    font = pygame.font.SysFont('Arial', 28)

    if game_over:
        message = f"Player {winner} Wins!" if winner else "It's a Draw!"
        if winner:
            score[winner] += 1
        text = font.render(message, True, TEXT_COLOR)
    else:
        time_left = max(0, TURN_TIME_LIMIT - int(time.time() - turn_start_time))
        text = font.render(f"Player {player}'s Turn - {time_left}s", True, TEXT_COLOR)

    screen.blit(text, text.get_rect(center=(WIDTH // 2, WIDTH + 30)))

    # Draw scores
    score_font = pygame.font.SysFont('Arial', 22)
    score_text = score_font.render(f"Score  X: {score['X']}  O: {score['O']}", True, TEXT_COLOR)
    screen.blit(score_text, (20, WIDTH + 60))

    # Draw Play Again button
    if game_over:
        button_rect = pygame.Rect(WIDTH // 2 - 100, WIDTH + 50, 200, 50)
        mouse_pos = pygame.mouse.get_pos()
        color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(screen, color, button_rect)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)

        button_font = pygame.font.SysFont('Arial', 24)
        button_text = button_font.render("Play Again", True, BUTTON_TEXT_COLOR)
        screen.blit(button_text, button_text.get_rect(center=button_rect.center))


def reset_game():
    global board, player, game_over, winner, win_coords, turn_start_time
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player = 'X'
    game_over = False
    winner = None
    win_coords = None
    turn_start_time = time.time()
    screen.fill(BG_COLOR)
    draw_lines()


# Initial draw
draw_lines()

# === Main Game Loop ===
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            if mouseY < WIDTH:
                row, col = mouseY // SQUARE_SIZE, mouseX // SQUARE_SIZE
                if board[row][col] is None:
                    board[row][col] = player
                    result = check_win()
                    if result:
                        winner = result
                        game_over = True
                    elif is_board_full():
                        game_over = True
                    else:
                        player = 'O' if player == 'X' else 'X'
                        turn_start_time = time.time()

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            mouseX, mouseY = event.pos
            if pygame.Rect(WIDTH // 2 - 100, WIDTH + 50, 200, 50).collidepoint((mouseX, mouseY)):
                reset_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()

    if not game_over and time.time() - turn_start_time >= TURN_TIME_LIMIT:
        player = 'O' if player == 'X' else 'X'
        turn_start_time = time.time()

    draw_figures()
    if win_coords:
        start_cell, end_cell = win_coords
        start_pos = (start_cell[0] * SQUARE_SIZE + SQUARE_SIZE // 2, start_cell[1] * SQUARE_SIZE + SQUARE_SIZE // 2)
        end_pos = (end_cell[0] * SQUARE_SIZE + SQUARE_SIZE // 2, end_cell[1] * SQUARE_SIZE + SQUARE_SIZE // 2)
        draw_win_line(start_pos, end_pos)

    draw_status()
    pygame.display.update()
