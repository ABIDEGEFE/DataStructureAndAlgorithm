class Solution(object):
    def pacificAtlantic(self, heights):

        atlantic_reachable = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        pacific_reachable = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def helper(row, col, reachable_ocean):
            reachable_ocean[row][col] = True

            for r, c in directions:
                n_row, n_col = row+r, col+c
                if 0 <= n_row < len(heights) and 0 <= n_col < len(heights[0]) and not reachable_ocean[n_row][n_col] and heights[n_row][n_col] >= heights[row][col]:
                    helper(n_row, n_col, reachable_ocean)

        for row in range(len(heights)):
            helper(row,0, pacific_reachable)
            helper(row, len(heights[0]) - 1, atlantic_reachable)

        for col in range(len(heights[0])):
            helper(0, col, pacific_reachable)
            helper(len(heights)-1, col, atlantic_reachable)

        res = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if pacific_reachable[row][col] and atlantic_reachable[row][col]:
                    res.append([row, col])

        return res
        
        
        