import random

def input_to_int(var):
    while True:
        e = input(f"{var}: ")
        try:
            e = int(e)
        except ValueError: 
            print(f"{var} must be an integer")
        else:
            break
    return e

def gen_maze():
    width = input_to_int("width")
    height = input_to_int("height")
    base_maze = []
    for h in range(height):
        base_maze.append([])
        for l in range(width):
            base_maze[h].append(0)

    row = -1
    while row < height-1:
        row += 1
        if row > 0 and row != height-1:
            paths = random.randint(1,width)
        else:
            paths = 1
        follows_path = False

        while paths > 0:
            while follows_path == False:
                next_space = random.randint(0,width-1)
                if base_maze[row-1][next_space] == 1 and base_maze[row][next_space] != 1 or row == 0:
                        follows_path = True
                        paths -= 1
                        break
                if next_space + 1 < width and base_maze[row][next_space] != 1:
                    if  base_maze[row][next_space+1] == 1:
                        follows_path = True
                        paths -= 1       
                        break               
                if next_space - 1 > 0 and base_maze[row][next_space] != 1:
                    if base_maze[row][next_space-1] == 1:
                        follows_path = True
                        paths -= 1
                        break
          
            base_maze[row][next_space] = 1
            follows_path = False   

    return (base_maze)

def print_maze(var):
    n = -1
    for e in var:
        n += 1
        print(var[n]) 

maze = gen_maze()
print_maze(maze)