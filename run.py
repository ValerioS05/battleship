#module imports
import random


def make_grid(size):
    """
    Create a grid with "~~" based on size choosen
    """
    return [["~~"] * size for i in range(size)]

def print_grid(grid):
    """
    Printing the grid using join() for better readability
    Using a second print for spacing
    """
    for row in grid:
        print(" ".join(row))
    print()
# initialize game letting the user choose between two grids
def game():
        """
        Initialize main function
        """
        while True:
            try:
                choose_size = int(input("Choose the board size: 1 for small, 2 for large: "))
                if choose_size == 1:
                    size = 5
                    break
                elif choose_size == 2:
                    size = 10
                    break
                else:
                    print("Invalid choice! Please enter 1 or 2.")
            except ValueError:
                print("Invalid choise! Please enter 1 or 2.")
        grid_palyer = make_grid(size)
        grid_cpu = make_grid(size)
        print(f"The {size}x{size} board is ready!")  
        print_grid(grid_palyer)
        print_grid(grid_cpu)
# call the game function
game()