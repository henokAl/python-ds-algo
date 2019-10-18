from collections import namedtuple, deque

# matrix is boolean 2D matrix. We want the region associated with some coordinate to be
# repainted
# O(m+n) time complexity
Coordinate = namedtuple('Coordinate', ('x', 'y'))


class Solution(object):
    def flip_color(self, x, y, matrix):
        color = matrix[x][y]
        q = deque([Coordinate(x, y)])
        matrix[x][y] = 1 - matrix[x][y]
        while q:
            x, y = q.popleft()
            for d in (0, 1), (0, -1), (1, 0), (-1, 0):
                next_x, next_y = x + d[0], y + d[1]
                if self.valid_cell(next_x, next_y, matrix, color):
                    matrix[next_x][next_y] = 1 - matrix[next_x][next_y]
                    q.append(Coordinate(next_x, next_y))

    def valid_cell(self, next_x, next_y, matrix, color):
        return 0 <= next_x < len(matrix) and 0 <= next_y < len(matrix[next_x]) and matrix[next_x][next_y] == color
