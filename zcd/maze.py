''' maze'''
#! /usr/bin/env python
import random
import time
def main():
    ''' main '''
    maze = Maze(20, 20)
    maze.print_list()
    func_start_time = time.time()
    path = maze.across_maze()
    print time.time() - func_start_time
    print path
    maze.across_map()

class Maze(object):
    ''' Maze '''
    def __init__(self, start=5, end=9):
        self.maze_list = self.random_list(start, end)
        half_row = 0 if self.maze_list is None else len(self.maze_list) / 2
        half_col = 0 if self.maze_list is None or self.maze_list[0] is None else len(self.maze_list[0]) / 2
        self.__row, self.__col = half_row, half_col
        self.__maze_path = [(half_row, half_col)]
        # start point is 1
        self.maze_list[self.__row][self.__col] = 1

    def random_list(self, start=5, end=5):
        ''' create list '''
        row = random.randint(start, end)
        col = random.randint(start, end)
        # row, col = 8, 8
        listdd = []
        for r in range(0, row):
            col_list = []
            for c in range(0, col):
                col_list.append(random.randint(0, 1))
            listdd.append(col_list)
        return listdd

    def print_list(self, array=None):
        ''' print list @param [] '''
        if array is None:
            array = self.maze_list
        print len(array), 'x', len(array[0])
        for row in array:
            for col in row:
                print col,
            print

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

                self.maze_list[self.__row][self.__col] = 1
                if is_across:
                    self.__maze_path.append((self.__row, self.__col))
                    if self._len_maze_path() > 3:
                        if self._is_neighbor(self.__maze_path[-1], self.__maze_path[-4]):
                            self.__maze_path.remove(self.__maze_path[-2])
                            self.__maze_path.remove(self.__maze_path[-2])
                else:
                    # back
                    self.__maze_path.pop()
                    # update postion
                    if self._len_maze_path() > 0:
                        self.__row, self.__col = self.__maze_path[-1]
                    else:
                        return self.__maze_path
            return self.__maze_path

    def _len_maze_path(self):
        return len(self.__maze_path)

    def _is_neighbor(self, tup1, tup2):
        x_distance = abs(tup1[0] - tup2[0])
        y_distance = abs(tup1[1] - tup2[1])
        is_neighbor = (x_distance == 0 and y_distance == 1) or (x_distance == 1 and y_distance == 0)
        return is_neighbor

    def across_map(self):
        ''' print map list '''
        if self._len_maze_path() > 0:
            map_list = self.map_path_list()
            for point in self.__maze_path:
                row, col = point
                map_list[row][col] = 0
            self.print_list(map_list)
        else:
            print 'block maze'

    def map_path_list(self):
        ''' create list '''
        row = len(self.maze_list)
        col = len(self.maze_list[0])
        return [[1] * col for r in range(0, row)]


main()
'''
0 1 0 0 1 0 0 1 0 0
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 1 0 0 1 1
0 1 1 0 0 1 0 0 0 1
1 0 1 0 0 0 0 1 0 1
0 1 1 0 0 1 0 1 1 0
0 0 1 1 1 1 0 1 0 0
0 0 0 1 0 1 1 0 1 0
1 0 1 1 1 1 0 0 0 0
0 0 1 0 0 1 1 1 1 1

0 0 1 1 1 1 1 0 1 0
1 1 1 0 0 1 0 1 1 0
0 1 1 1 1 0 1 0 1 0
1 0 1 1 1 0 0 0 1 1
1 1 0 0 1 0 0 0 1 0
0 1 1 1 0 1 0 1 1 0
1 0 0 1 0 0 0 0 1 0
0 1 1 0 0 0 1 1 0 1
0 0 0 1 0 0 1 1 0 0
0 0 1 1 0 0 1 0 1 1
'''