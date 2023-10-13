# Running Game Automation

Automate a running game by analyzing specific pixel colors and controlling character movement accordingly. This script checks for obstacles and adjusts the character's position to navigate through them.

## Overview

This project automates a running game where the character needs to avoid obstacles by moving left or right. The script continuously checks specific pixels on the screen to detect obstacles and respond accordingly.

## Requirements

To run this automation script, you need:

- Python 3.x
- Required Python packages (`pyautogui`, `keyboard`, `win32api`, `win32con`)

Install the required packages using pip:

```bash
pip install pyautogui keyboard pywin32
```

## Usage
Clone this repository to your local machine.
```bash
git clone https://github.com/AnjanaKvd/megarun2-auto-script-python.git
```
Navigate to the project directory.
```bash
cd running-game-automation
```
Run the script by executing the following command:
```bash
python run_game_automation.py
```
The script will start monitoring the game screen and automatically control character movement to avoid obstacles.
## How It Works
- The script uses pixel color analysis at predefined positions to detect obstacles:
- The middle position of the character.
- The left position relative to the character.
- The right position relative to the character.

If an obstacle is detected at the current position, the script moves the character to the opposite side (left to right, or right to left).

The script continuously checks for obstacles and adjusts the character's position accordingly.

## Configuration
You can customize the script 

