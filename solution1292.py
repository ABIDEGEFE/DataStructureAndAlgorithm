class Solution(object):
    def maxSideLength(self, mat, threshold):

        def get_sum(prefix, r1, c1, r2, c2):

            total = prefix[r2][c2]

            if r1 > 0:
                total -= prefix[r1 - 1][c2]
            if c1 > 0:
                total -= prefix[r2][c1 - 1]
            if c1 > 0 and r1 > 0:
                total += prefix[r1 - 1][c1 - 1]

            return total

        n, m = len(mat), len(mat[0])
        prefix = [[0]*m for i in range(n)]

        for i in range(n):
            for j in range(m):
                prefix[i][j] = mat[i][j]
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
        side_len = 0
        for row in range(n):
            for col in range(m):
                row2 = row
                col2 = col
                length = 0
                total = mat[row][col]
                while total <= threshold and row2 < n and col2 < m:

                    total = get_sum(prefix, row, col, row2, col2)
                    row2 += 1
                    col2 += 1
                    if total <= threshold:
                        length += 1
                    side_len = max(side_len, length)

        return side_len
       
        