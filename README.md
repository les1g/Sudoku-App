# Sudoku Application

This Sudoku application is a graphical user interface (GUI) implementation of the classic Sudoku game using Python's Tkinter library. The application allows users to generate random Sudoku puzzles, solve them, and interactively fill in the grid.

<div style="display: flex; justify-content: center; gap: 10px;">
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/b22a4881-c3a8-4e6e-8d0e-6f41c412e79c" />
  <img width="400" alt="image" src="https://github.com/user-attachments/assets/81cd04fa-d360-43e3-8f6d-11dd50e7a329" />
</div>

**App Module**: User-friendly interface with input validation and a Visual representation of the Sudoku grid.

**Logic Module**: Generate random Sudoku puzzles and solve existing Sudoku puzzles.
  
## What I Learned  
Working on this Sudoku application taught me how to separate puzzle logic from the graphical interface. I gained hands-on experience with Python’s Tkinter library, event-driven programming, and managing widgets with grid layouts. I also learned how to work with 2D arrays for Sudoku grids, validate user input, and integrate external libraries like NumPy and dokusan.

## Installation

To run this application, you need to have Python installed on your machine. You can install the required dependencies using the pip package manager. 

1. Clone the repository: 
   ```
   git clone https://github.com/les1g/Sudoku-App.git
   cd sudoku-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To start the application, run the following command:

```
python app_test.py
```

This will launch the Sudoku application window where you can generate puzzles and solve them.
