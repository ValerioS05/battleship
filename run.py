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
    in {i + 0 : 2} --> 0 stands for the initial number and 2 stands for the width occupied
    choose the 2 to give enough width to be inline with columns 
    chr 65 = A (uppercase) iterates through the rows + index
    added a empty print to add spacing
    """
    size = len(grid)
    print("  " + " ".join(f"{i+0:2}" for i in range(size)))
    for index, row in enumerate(grid):
        print(f"{chr(65+index)}  " + " ".join(row))
    print()

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
            if hide:
                grid[row][col] = "~~"


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
        # number of ships that i want randomly placed
        ships_num = 5
        #Placing ships related to player/cpu grip and number of ships wanted
        place_all_ships(grid_palyer,ships_num,hide=False)
        place_all_ships(grid_cpu,ships_num)
        print(f"The {size}x{size} board is ready!")  
        print_grid(grid_palyer)
        print_grid(grid_cpu)
# call the game function
game()