class Solution(object):
    def convertToBase7(self, num):
        result = ""
        isNegative = False
        if num < 0:
            num = -1*num
            isNegative = True
        if num == 0:
            return "0"
        while num != 0:
            r = num % 7
            result = str(r) + result
            num = int(num / 7)
        if isNegative:
            return "-"+result
        return result
        
        