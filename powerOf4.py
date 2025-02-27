class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        log_value = log10(n)/log10(4)
        return log_value == int(log_value)
        