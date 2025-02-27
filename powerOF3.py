class Solution(object):
    
    def isPowerOfThree(self, n):
        ix = 0
        while 3**ix <= n:
            if 3**ix == n:
                return True
            ix += 1
        return False
        
        
        