# Desktop Graphical Rock-Paper-Scissors Game

An interactive, graphical desktop application implementing the classic Rock-Paper-Scissors game with state management, score tracking, and smooth image rendering using Pillow.

Project Overview:
This project provides a clean desktop interface built using Python's native Tkinter library paired with Pillow for image manipulation. It features automated computer choice generation using Python's pseudo-random number generator, interactive button triggers, and real-time score tracking.

Technologies Used:
Python (Core application logic)
Tkinter (Desktop GUI layout, widgets, canvas, and event handling)
Pillow / PIL (High-resolution image processing, resizing, and rendering of game assets)
Random Module (Algorithmic computer opponent decision making)

Key Features:
1. Interactive UI: Clean layout with custom button graphics (`rock_button1.jpeg`, `paper_button1.jpeg`, `scissors_button1.jpeg`) and score badges.
2. Dynamic Image Rendering: Utilizes PIL to dynamically load and display state images (`default.jpeg`, `rock.jpeg`, `paper.jpeg`, `scissor.jpeg`) for                              both player and computer choices.
3. State & Score Tracking: Automatically calculates win/loss/tie outcomes and increments cumulative score counters during active sessions.
4. Robust Event Handling: Implements smooth user input responses with error-free image resource management.

How to Run the Code
1. Clone or download the repository files.
2. Install the required image library:
   ```bash
   pip install pillow

   python game_project.py
