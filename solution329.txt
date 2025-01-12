class Solution(object):
    def longestIncreasingPath(self, matrix):

        path = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def helper(row, col):
            if path[row][col] != -1:
                return path[row][col]
            max_length = 1

            for r, c in direction:
                new_row, new_col = row+r, col+c
                if 0 <= new_row <= len(matrix)-1 and 0 <= new_col <= len(matrix[0]) - 1 and matrix[new_row][new_col] > matrix[row][col]:
                    max_length = max(max_length, helper(new_row, new_col)+1)

            path[row][col] = max_length
            return max_length

        max_length = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                max_length = max(max_length, helper(row, col))

        return max_length
      
      
        