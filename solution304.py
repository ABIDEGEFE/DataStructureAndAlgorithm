class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix

        n, m = len(self.matrix), len(self.matrix[0])
        self.p_sum = []
        for i in range(n):
            self.p_sum.append([0] * m)
        # print(p_sum)
        for i in range(n):
            for j in range(m):
                self.p_sum[i][j] = self.matrix[i][j]
                if i > 0:
                    self.p_sum[i][j] += self.p_sum[i - 1][j]
                if j > 0:
                    self.p_sum[i][j] += self.p_sum[i][j - 1]
                if i > 0 and j > 0:
                    self.p_sum[i][j] -= self.p_sum[i - 1][j - 1]


    def sumRegion(self, row1, col1, row2, col2):

        total = self.p_sum[row2][col2]

        if row1 > 0:
            total -= self.p_sum[row1 - 1][col2]
        if col1 > 0:
            total -= self.p_sum[row2][col1 - 1]
        if col1 > 0 and row1 > 0:
            total += self.p_sum[row1 - 1][col1 - 1]

        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)