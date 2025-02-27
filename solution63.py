class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
                
        if obstacleGrid[0][0] == 1:
            return 0

        n, m = len(obstacleGrid[0]), len(obstacleGrid)
        res = [0]*n
        res[0] = 1

        for rw in range(m):
            for cl in range(n):
                if obstacleGrid[rw][cl] == 1:
                    res[cl] = 0
                elif cl > 0:
                    res[cl] += res[cl-1]

        return res[-1]
        