
# Number Combat Game 🎮

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Complete-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-yellowgreen)

A Python-based combat game with graphical user interface where players fight numbers to survive through 20 attempts. Built with Tkinter for GUI and featuring progressive difficulty levels.


## 📖 Overview

This project combines strategic number combat with GUI elements to create an engaging gaming experience. Players must carefully select numbers from generated enemies to survive through 20 rounds while managing their life score.

## ✨ Features

- 🎯 Progressive difficulty with 4 enemy tiers
- 🖥️ Tkinter GUI with real-time updates
- 📊 Game state auto-saving
- ✅ Input validation and error handling
- 📈 Attempt tracking system
- 🏆 Victory/defeat conditions
- 📂 Automatic game log generation

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chamudithaweeramanthri/number-combat-game.git
   cd number-combat-game
Install requirements
bash
Copy
pip install tkinter

Note: Tkinter is usually included with Python. For Linux users:
bash
Copy
sudo apt-get install python3-tk

🕹️ Usage
Start the game:

bash
Copy
python game_gui.py
Game flow:

Enter player name

Select numbers from displayed enemies

Survive through 20 attempts

Manage life score strategically

Avoid selecting numbers larger than current life score

📸 **Screenshots**
<br><br>
![image](https://github.com/user-attachments/assets/cc194bca-786b-42c3-ba5f-76d9cff55880)
<br><br>
![image](https://github.com/user-attachments/assets/d9e4ebb5-9d61-42bb-b449-7665004eae8e)
<br><br>
![image](https://github.com/user-attachments/assets/36143ca6-10ec-4fa1-bdff-31124b41b518)

🧠 **Game Logic**
Enemy Generation:

Attempts 1-5: 15-100

Attempts 6-10: 250-2000

Attempts 11-15: 3000-10,000

Attempts 16-20: 20,000-100,000

Life Score Mechanics:

Initial random value (1-50)

Increases with successfully defeated numbers

Game ends if selected number > life score

📂 **Repository Structure**
Copy
number-combat-game/<br>
├── game_gui.py       # Main GUI application.<br>
├── game_modules.py   # Core game logic module<br>
├── README.md         # This documentation<br>
└── requirements.txt  # Dependency list

Happy gaming! 🚀 If you survive all 20 attempts, you'll be a number combat master! 💪

