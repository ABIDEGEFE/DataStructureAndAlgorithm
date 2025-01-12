class Solution(object):
    def hammingDistance(self, x, y):

        result = x^y
        return str(bin(result)).count('1')

        
        
        