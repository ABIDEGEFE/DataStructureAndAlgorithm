class Solution(object):
    def minDistance(self, word1, word2):

        row, col = len(word1), len(word2)
        res = [[0 for _ in range(col+1)]for _ in range(row+1)]

        for rows in range(1, row+1):
            res[rows][0] = res[rows-1][0]+1
        for cols in range(1, col+1):
            res[0][cols] = res[0][cols-1]+1

        for r in range(1, row+1):
            for c in range(1, col+1):
                if word1[r-1] == word2[c-1]:
                    res[r][c] = res[r-1][c-1]
                else:
                    res[r][c] = min(res[r][c-1], res[r-1][c], res[r-1][c-1])+1

        return res[row][col]
    
        