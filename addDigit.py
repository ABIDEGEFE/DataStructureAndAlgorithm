class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        return 1 + (num-1)%9