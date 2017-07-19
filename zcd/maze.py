#! /usr/bin/env python
import random

def main():
    ''' main '''
    arraydd = random_list(5,9)
    print_list(arraydd)
    maze = Maze(arraydd)
    print maze.across_maze()


def random_list(start=5, end=5):
    ''' create list '''
    row = random.randint(start, end)
    col = random.randint(start, end)
    # row, col = 8, 5
    listdd = []
    for r in range(0, row):
        col_list = []
        for c in range(0, col):
            col_list.append(random.randint(0, 1))
        listdd.append(col_list)
    return listdd

def print_list(array):
    ''' print list @param [] '''
    print len(array), len(array[0])
    for row in array:
        for col in row:
            print col,
        print

class Maze():
    ''' Maze '''
    def __init__(self, maze_list):
        self.maze_list = maze_list
        half_row = 0 if self.maze_list is None else len(self.maze_list) / 2
        half_col = 0 if self.maze_list is None or self.maze_list[0] is None else len(self.maze_list[0]) / 2
        self.__row, self.__col = half_row, half_col
        self.__maze_path = [(half_row, half_col)]
        # start point is 1
        self.maze_list[self.__row][self.__col] = 1
    
    def across_maze(self):
        ''' across_maze -> list '''
        if self.maze_list is None:
            return []
        else:
            while (0 < self.__col < len(self.maze_list[0]) - 1) and (0 < self.__row < len(self.maze_list) - 1):
                is_across = False
                if   self.maze_list[self.__row][self.__col + 1] == 0:
                    self.__col += 1
                    is_across = True
                elif self.maze_list[self.__row + 1][self.__col] == 0:
                    self.__row += 1
                    is_across = True
                elif self.maze_list[self.__row][self.__col - 1] == 0:
                    self.__col -= 1
                    is_across = True
                elif self.maze_list[self.__row - 1][self.__col] == 0:
                    self.__row -= 1
                    is_across = True
                else:
                    pass

                if is_across:
                    self.__maze_path.append((self.__row, self.__col))
                    self.maze_list[self.__row][self.__col] = 1
                else:
                    self.maze_list[self.__row][self.__col] = 1
                    # back
                    self.__maze_path.pop()
                    # update postion
                    if len(self.__maze_path) > 0:
                        self.__row, self.__col = self.__maze_path[-1]
                    else:
                        return self.__maze_path
            return self.__maze_path

main()
