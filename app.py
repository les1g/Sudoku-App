# app_test.py
import tkinter as tk  # Import the Tkinter library for GUI development
from itertools import batched  # Import batched to split data into chunks
from logic import generate_sudoku, solve_sudoku  # Import functions from logic_test.py

# Define the main Sudoku game class
class SudokuGame:
    def __init__(self, master):  # Renamed from 'root' to avoid shadowing
        self.root = master  # Store the root window
        self.root.title("Sudoku")  # Set the window title
        self.root.geometry("800x900")  # Set the window size

        # Initialize board data as a 9x9 grid filled with '0' (empty cells)
        numbers = '0' * 81  # Create a string of 81 zeros
        self.board = [list(row) for row in batched(numbers, 9)]  # Convert to 2D list (9 rows of 9 cells)

        # Create a frame to hold the Sudoku grid
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(padx=20, pady=20)  # Add padding around the grid
        
        generate_button = tk.Button( # TODO: this function is being tested still 
            self.root,
            text="Generate Puzzle",
            font=("Arial", 16),
            command=self.load_generated_puzzle
        )
        generate_button.pack(pady=10)

        # Register the validation function with Tkinter
        # '%P' passes the new value of the Entry widget to the function
        self.validate_cmd = (self.root.register(self.validate_input), '%P')

        # Prepare to store Entry widgets for each cell
        self.cell_widgets = []
        self.render_board()  # Call method to render the grid visually
        
        solve_button = tk.Button( # TODO: this function is being tested still
            self.root,
            text="Solve Puzzle",
            font=("Arial", 16),
            command=self.solve_current_puzzle
        )
        solve_button.pack(pady=10)
    
    def load_generated_puzzle(self): # TODO: this function is being tested still 
        puzzle = generate_sudoku()  # Get a new puzzle
        self.board = [[str(cell) if cell != 0 else '' for cell in row] for row in puzzle]  # Convert to string grid
        self.update_board_display()
        
    def solve_current_puzzle(self): # TODO: this function is being tested still
        # Read current board from Entry widgets
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                cell_value = self.cell_widgets[i][j].get()
                row.append(int(cell_value) if cell_value.isdigit() else 0)
            puzzle.append(row)

        # Solve the puzzle using your logic
        solved = solve_sudoku(puzzle)

        # Update board with solved values
        self.board = [[str(cell) for cell in row] for row in solved]
        self.update_board_display()

    # Validation function to allow only digits 1–9 or empty string
    @staticmethod
    def validate_input(new_value):
        return new_value in '123456789' or new_value == ''

    # Method to render the 9x9 grid of cells
    def render_board(self):
        for i in range(9):  # Loop through rows
            row_widgets = []  # Store widgets for this row
            for j in range(9):  # Loop through columns
                value = self.board[i][j]  # Get the value for this cell

                # Create an Entry widget for user input
                entry = tk.Entry(
                    self.grid_frame,
                    width=2,  # Smaller width for tighter layout
                    font=("Arial", 28),  # Larger font for better visibility
                    justify="center",  # Center-align the text
                    bd=0.5,  # Border width
                    relief="solid",  # Solid border style
                    validate="key",  # Enable validation on key press
                    validatecommand=self.validate_cmd  # Use the registered validation function
                )

                # Insert value if not '0'
                if value != '0':
                    entry.insert(0, value)
                    entry.config(state="disabled", disabledforeground="black")  # Make fixed cells non-editable

                # Add padding to simulate 3x3 block separation
                pad_x = 4 if j % 3 == 0 else 2
                pad_y = 4 if i % 3 == 0 else 2

                # Place the Entry widget in the grid with padding
                entry.grid(row=i, column=j, padx=0, pady=0)
                row_widgets.append(entry)  # Store the widget

            self.cell_widgets.append(row_widgets)  # Add row to the widget list

    def update_board_display(self): # TODO: this function is being tested still 
        """Update the GUI to reflect the current state of the board."""
        for i in range(9):
            for j in range(9):
                entry = self.cell_widgets[i][j]
                entry.config(state="normal")  # Make editable before updating
                entry.delete(0, tk.END)
                value = self.board[i][j]
                if value != '':
                    entry.insert(0, value)
                    entry.config(state="disabled", disabledforeground="black")
                else:
                    entry.config(state="normal")
                
# Launch the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    game = SudokuGame(root)  # Instantiate the game
    root.mainloop()  # Start the Tkinter event loop