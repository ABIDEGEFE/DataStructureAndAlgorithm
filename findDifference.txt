class Solution(object):
    def findTheDifference(self, s, t):

        x = 0
        for i in s:
            x = x^ord(i)
        for j in t:
            x = x^ord(j)
        return chr(x)

        

     
        
        