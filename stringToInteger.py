class Solution(object):
    def myAtoi(self, s):

        s = s.lstrip()
        isNumber = False
        op = ""
        for i in s:
            if i.isdigit():
                op += i
                isNumber = True
            if not i.isdigit() and isNumber:
                break

        if not op:
            return 0
        
        ix = s.index(op)
       
        
        if "++"+op in s or "--"+op in s or "-+"+op in s or "+-"+op in s:
            return 0
        if "-" + op in s:
            op = "-"+op
            if int(op) < -2**31:
                return -2**31
            else:
                return int(op)
        if "+" + op in s and int(op) < (2**31)-1:
            return int(op)
        elif "+" + op in s and int(op) > (2 ** 31) - 1:
            return (2 ** 31) - 1
    
        
        if ix != 0:
            if not s[ix-1].isdigit():
                return 0
        if int(op) > (2**31)-1:
            return (2**31)-1
        else:
            return int(op)