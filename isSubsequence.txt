class Solution(object):
    def isSubsequence(self, s, t):

        ix = 0
        for i in t:
            if ix < len(s) and i == s[ix]:
                ix += 1

        return ix == len(s)

        



        