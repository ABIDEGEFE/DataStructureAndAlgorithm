class Solution(object):
    def addStrings(self, num1, num2):

        if len(num1) < len(num2):
            num1 = num1.zfill(len(num2))
        else:
            num2 = num2.zfill(len(num1))

        sum = ""
        isDouble = False
        n = 0
        ones = None
        tenth = None
        for i in range(len(num1)-1, -1, -1):
            if isDouble:
                n = int(num1[i]) + int(tenth)
                isDouble = False
            else:
                n = int(num1[i])
            res = n + int(num2[i])
            
            if len(str(res)) == 2 and i ==0:
                sum = str(res) + sum
            elif len(str(res)) == 2:
                ones = str(res)[-1]
                tenth = str(res)[0]
                isDouble = True
                sum = ones + sum
            
            else:
                sum = str(res) + sum

        return sum

        
            

                
            
            
        
        