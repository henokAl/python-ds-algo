from collections import namedtuple

Coordinates = namedtuple('Coordinates', ('x', 'y'))
WHITE, BLACK = range(2)


class Solution(object):
    def search_maze(self, src, dest, maze):
        path = list()
        if not self.helper(src, path, dest, maze):
            return []
        return path

    def helper(self, src, path, dest, maze):
        if not self.valid_path(src, maze):
            return False
        path.append(src)
        maze[src.x][src.y] = BLACK
        if src == dest:
            return True

        neighbour_coordinates = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for coord in neighbour_coordinates:
            if self.helper(Coordinates(src.x + coord[0], src.y + coord[1]), path, dest, maze):
                return True
        '''
         if any(map(self.helper, (Coordinates(src.x - 1, src.y),
                                  Coordinates(src.x + 1, src.y),
                                  Coordinates(src.x, src.y - 1),
                                  Coordinates(src.x, src.y + 1)
                                  path, dest, maze ))):
             return True
         '''
        # we could not find path
        del path[-1]
        return False

    def valid_path(self, src, maze):
        return 0 <= src.x < len(maze) and 0 <= src.y < len(maze[0]) and maze[src.x][src.y] == WHITE
