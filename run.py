#module imports
import random


def make_grid(size):
    """
    Create a grid with "~~" based on size choosen
    """
    return [["~~"] * size for i in range(size)]


def place_a_ship(grid, row, col):
    """
    Placing a signle ship 
    """
    grid[row][col] = "00"

def place_all_ships(grid, ships_num, hide=True):
    """
    Placing all the ships in the grid, ship cell size is 1 
    hide is used to hide ships (in game() is set to False in the grid_player )
    """
    size = len(grid)
    placed_ships = 0
    while placed_ships < ships_num:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if grid[row][col] == "~~":
            place_a_ship(grid,row,col)
            placed_ships +=1
            print(f"Placed ship at ({chr(65 + row)}, {col})")  # Debug: Print ship position
            if hide:
                grid[row][col] = "~~"

def where_to_shoot(size):
    """
    Get the selected cell that the user/cpu wants to shoot
    """
    while True:
        try:
            print("Choose where to shoot selecting a Row and a Column")
            row_input = input(f"Select the Row (A-{chr(65+size-1)}): ").upper()
            if "A" <= row_input <= chr(65 + size - 1):
                row = ord(row_input) - 65
                col_input = int(input(f"Select the Column (0-{size - 1}): "))
                if 0 <= col_input < size:
                    return row, col_input
            print("Invalid coordinates! Coordinates must be within the grid size!")
        except ValueError:
            print("Invalid input! Coordinates must be a displayed letter and displayed number!")
        
def check_shoot(grid, row, col):
    if grid[row][col] == "00":
        grid[row][col] = "XX"  # Hit
        return True
    else:
        grid[row][col] = "**"  # Miss
        return False

def print_grid(grid):
    size = len(grid)
    print("  " + " ".join(f"{i+0:2}" for i in range(size)))
    for index, row in enumerate(grid):
        print(f"{chr(65+index)}  " + " ".join(row))
    print()

def game():
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
            print("Invalid choice! Please enter 1 or 2.")
    grid_palyer = make_grid(size)
    grid_cpu = make_grid(size)
    ships_num = 5
    place_all_ships(grid_palyer, ships_num, hide=False)
    place_all_ships(grid_cpu, ships_num, hide=False)
    print(f"The {size}x{size} board is ready!")  
    print_grid(grid_palyer)
    print_grid(grid_cpu)

    while True:
        row, col = where_to_shoot(size)
        print(f"Shooting at ({chr(65 + row)}, {col})")
        if check_shoot(grid_cpu, row, col):
            print(f"Hit at {chr(65 + row)},{col}")
        else:
            print(f"Missed at {chr(65 + row)},{col}")
        print_grid(grid_cpu)  # Debug: Print grid after each shot

# Call the game function
game()