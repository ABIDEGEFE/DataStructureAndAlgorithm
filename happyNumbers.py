class Solution(object):
    def isHappy(self, n):
        
        ls = []
        while n != 1 and n not in ls :
            ls.append(n)
            res = 0
            while n != 0:
                modulo = n % 10
                res += modulo*modulo
                n = n//10
            n = res

        return n == 1

            
            
        
        