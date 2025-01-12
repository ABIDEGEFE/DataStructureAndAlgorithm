class Solution(object):
    def findMaxForm(self, strs, m, n):

        res = [[0]*(n+1) for c in range(m+1)]
        for st in strs:
            c0 = st.count("0")
            c1 = st.count("1")
            for i in range(m, c0-1, -1):
                for j in range(n, c1-1, -1):
                    res[i][j] = max(res[i][j], res[i-c0][j-c1]+1)

        return res[m][n]
     
     
        