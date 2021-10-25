class Solution(object):
    def solution1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        new_grid = np.zeros([len(grid) + 2, len(grid[1]) + 2])
        perimeter = 0
        new_grid[1:new_grid.shape[0] - 1, 1:new_grid.shape[1] - 1] = np.array(grid)
        for row in range(1, new_grid.shape[0] - 1):
            for col in range(1, new_grid.shape[1] - 1):
                if new_grid[row, col] == 1:
                    perimeter += int(new_grid[row - 1, col] == 1)
                    perimeter += int(new_grid[row, col - 1] == 1)
                    perimeter += int(new_grid[row + 1, col] == 1)
                    perimeter += int(new_grid[row, col + 1] == 1)
        return perimeter

if __name__ == '__main__':
    print (Solution().solution1([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))