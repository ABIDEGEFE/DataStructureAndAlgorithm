class Solution(object):
    def divide(self, dividend, divisor):

        if dividend == -2**31 and divisor == -1:
            return (2**31)-1
        if abs(divisor) == 1:
            return dividend * divisor
        
        is_negative = False

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            is_negative = True
        
        dividend, divisor = abs(dividend), abs(divisor)
        q = 0
        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                q += 1 << i
            
        if is_negative:
            q = -1*q
        q = min(q, 2**31)
        return max(-2**31, q)