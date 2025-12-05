from utils.read import read_file
from typing import List, Tuple

def create_2d_grid(_input):
    _grid = []
    for _row in _input:
        row = []
        for _cell in _row:
            row.append(_cell)
        _grid.append(row)
    return _grid

def get_surrounding_entries(_grid: List[List[str]], row: int, col: int) -> List[Tuple[int, int]]:
    surrounding = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_row, new_col = row + i, col + j
            if 0 <= new_row < len(_grid) and 0 <= new_col < len(_grid[0]):
                surrounding.append((new_row, new_col))
    return surrounding

def part_one(_grid):
    accessible = 0
    for row in range(len(_grid)):
        for col in range(len(_grid[0])):
            if _grid[row][col] == "@":
                surroundingEntries = []
                surrounding = get_surrounding_entries(_grid, row, col)
                for x,y in surrounding:
                    if _grid[x][y] == "@":
                        surroundingEntries.append(_grid[x][y])
                if len(surroundingEntries) < 4:
                    accessible += 1
    print(f"Part 1 - Rolls that the forklift can access: {accessible}.")


def part_two(_grid):
    accessible = 0
    keepGoing = True
    rounds = 0
    while keepGoing:
        rounds += 1
        removed = 0
        for row in range(len(_grid)):
            for col in range(len(_grid[0])):
                if _grid[row][col] == "@":
                    surroundingEntries = []
                    surrounding = get_surrounding_entries(_grid, row, col)
                    for x, y in surrounding:
                        if _grid[x][y] == "@":
                            surroundingEntries.append(_grid[x][y])
                    if len(surroundingEntries) < 4:
                        accessible += 1
                        _grid[row][col] = "."
                        removed += 1
        if removed == 0:
            keepGoing = False
    print(f"Part 2 - Rolls that the forklift can access: {accessible}, in {rounds} rounds.")


if __name__ == "__main__":
    stringInput = read_file(4, "string", False)
    grid = create_2d_grid(stringInput)
    part_one(grid)
    part_two(grid)
