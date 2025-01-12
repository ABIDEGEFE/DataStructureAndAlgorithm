class Solution(object):
    def arrangeCoins(self, n):
        sum = 0
        ix = 1
        while True:
            sum += ix
            if sum == n:
                return ix
            if n < sum:
                return ix-1
            ix += 1


        