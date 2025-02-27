class Solution(object):
    def transpose(self, matrix):
        nums = [[] for i in range(len(matrix[0]))]

        for items in matrix:
            ix = 0
            for j in items:
                nums[ix].append(j)
                ix += 1

        return nums
        