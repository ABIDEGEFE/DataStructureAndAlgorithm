class Solution(object):
    def combine(self, n, k):

        res = []
        def helper(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return

            for i in range(start, n+1):
                comb.append(i)
                helper(i+1, comb)
                comb.pop()

        helper(1, [])

        return res
     
        