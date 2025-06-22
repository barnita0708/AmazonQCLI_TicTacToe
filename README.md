# 🎮 Tic-Tac-Toe Game (Built with Amazon Q CLI + Pygame)

A beautiful and modern two-player **Tic-Tac-Toe game** built using **Amazon Q CLI** and the **Pygame** library. This game provides a fun way to play classic tic-tac-toe with enhancements such as scoring, win-line highlighting, time-limited turns, and a polished user interface.

---

## 🛠️ Built With

- 🧠 **Amazon Q CLI** – for AI-driven development and project scaffolding
- 🎮 **Python (Pygame)** – for game rendering and logic
- 💻 Designed for desktops (Windows/macOS/Linux)

---

## ✨ Features

- ✅ Classic 3x3 Tic-Tac-Toe board
- 🎯 Win detection with **highlighted winning lines**
- ⏱️ **Turn timer** (optional: 10 seconds per move)
- 🧮 **Score tracking** for Player X and Player O
- 🖱️ Mouse-based input with visual feedback
- 🔁 **Reset/Replay** functionality via button or `R` key
- 🎨 Clean, modern UI with vibrant color themes
- 🪄 Easy customization of theme, size, and behavior

---

## 📦 Requirements

- Python 3.7+
- Pygame (installed via pip)
- Amazon Q CLI (for development automation, optional for running)

---

## 🔧 Installation

1.Clone this repository
```bash
  git clone https://github.com/barnita0708/AmazonQCLI_TicTacToe.git
```
2.Install required Dependencies
```bash
# Using pip
pip install pygame

# Or using apt on Debian/Ubuntu
sudo apt-get install python3-pygame
```
3.Run the game
```bash
python3 tttgame.py

or

python tttgame.py
```
## 🎮 How to Play
Player X starts the game.

Click any empty square to place your mark.

Players alternate turns until one wins or the board is full.

A message will appear if someone wins or if it’s a draw.

To play again, click the “Play Again” button or press the R key.

⏳ Each player has 10 seconds to make their move (can be changed in code).

## 📁 Code Structure

```
AmazonQCLI_TicTacToe/
├── tttgame.py          # Main game script
├── README.md           # Game documentation
├── assets/             # (Optional) sound files or images
└── prompt.txt          # Prompt used in Q CLI to generate the game
```
## 🎨 Customization
You can easily customize the game:

Colors: Modify the color constants at the top of ```game.py```

Board size: Change ```BOARD_SIZE``` for larger grids (e.g. 4x4)

Timer: Adjust ```TURN_TIME_LIMIT```

Sound: Add sound effects in the ```assets/``` folder and play them via ```pygame.mixer```

## 📜 License
This project is open-source and available under the MIT License.

## ✒ Blog Link 

Here's

## 🙏 Acknowledgements
Amazon Q CLI – for AI-assisted development workflow

Pygame – for 2D game rendering

Special thanks to the open-source Python community ❤️

