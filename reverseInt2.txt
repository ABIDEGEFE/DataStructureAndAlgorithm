class Solution(object):
    def reverse(self, x):
        sum = 0
        isNegative = False
        if x < 0:
            isNegative = True
            x = -1*x
        while x > 0:

            md = x%10
            sum = (sum*10)+md

            x = x//10

        if sum > (1 << 31) - 1 or -1*sum <= -(1 << 31):
            return 0
        if isNegative:
            return -1*sum
        if sum > (1 << 31) - 1 or sum <= -(1 << 31):
            return 0
        return sum
        