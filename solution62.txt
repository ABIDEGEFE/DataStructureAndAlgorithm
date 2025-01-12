class Solution(object):
    def uniquePaths(self, m, n):
        
        i = 0
        res = [1] * m

        while i < n - 1:
            for j in range(1, m):
                res[j] += res[j - 1]
            i += 1
        
        return res[-1]
        