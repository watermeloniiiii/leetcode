class Solution(object):
    def solution1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # import numpy as np
        # new_grid = np.zeros([len(grid) + 2, len(grid[1]) + 2])
        # perimeter = 0
        # new_grid[1:new_grid.shape[0] - 1, 1:new_grid.shape[1] - 1] = np.array(grid)
        # for row in range(1, new_grid.shape[0] - 1):
        #     for col in range(1, new_grid.shape[1] - 1):
        #         if new_grid[row, col] == 1:
        #             perimeter += int(new_grid[row - 1, col] == 1)
        #             perimeter += int(new_grid[row, col - 1] == 1)
        #             perimeter += int(new_grid[row + 1, col] == 1)
        #             perimeter += int(new_grid[row, col + 1] == 1)
        # return perimeter


        count = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        def isValidPos(i, j):
            nonlocal row, col, count
            # if the position goes out of the bounds of grid return False else return True
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            return True

        def recursive(x, y):
            nonlocal count, visited
            if not isValidPos(x, y) or visited[x][y] == True or grid[x][y] == 0:
                return
            visited[x][y] = True
            if not isValidPos(x-1, y) or grid[x - 1][y] == 0:
                count += 1
            if not isValidPos(x+1, y) or grid[x + 1][y] == 0:
                count += 1
            if not isValidPos(x, y-1) or grid[x][y - 1] == 0:
                count += 1
            if not isValidPos(x, y+1) or grid[x][y + 1] == 0:
                count += 1

            recursive(x - 1, y)
            recursive(x + 1, y)
            recursive(x, y - 1)
            recursive(x, y + 1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    recursive(i, j)
        return count
if __name__ == '__main__':
    print (Solution().solution1([[0,1,0,],[1,1,1,],[0,1,0,],[1,1,0,]]))