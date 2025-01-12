class Solution(object):
    def numIslands(self, grid):

        if not grid:
            return 0
        def helper_dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"

            helper_dfs(i+1, j)
            helper_dfs(i-1, j)
            helper_dfs(i, j+1)
            helper_dfs(i, j-1)

        island = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    island += 1
                    helper_dfs(row, col)

        return island

        
       
        