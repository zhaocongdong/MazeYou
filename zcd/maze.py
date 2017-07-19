#! /usr/bin/env python

class Maze():
    ''' Maze '''
    def __init__(self, maze_list):
        self.maze_list = maze_list
        halfl = len(self.maze_list) / 2
        self.__col, self.__row, self.__maze_path = halfl, halfl, [(halfl, halfl)] 
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

def main():
    ''' main '''
    arraydd = [[0, 1, 1, 1, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 1, 1, 1, 0]]
    for row in arraydd:
        for col in row:
            print col,
        print
    maze = Maze(arraydd)
    print maze.across_maze()

main()
'''
0 1 1 1 1 1 1 1 1 1 1
0 1 0 1 2 2 1 0 0 0 0
0 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 0 0 1 0 0 0
0 1 0 1 1 0 0 1 1 0 0
0 1 0 1 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 0 0 1 0 0 0
0 1 0 1 1 1 0 1 1 0 0
0 1 0 1 0 0 0 0 0 0 0
'''