class Solution(object):
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for j in range(1, m):
            grid[j][0] += grid[j-1][0]

        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])

        return grid[m-1][n-1]
        
      
        