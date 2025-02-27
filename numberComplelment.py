class Solution(object):
    def findComplement(self, num):
         
        res = "0b"
        binary = bin(num)

        for i in range(2, len(binary)):
            if binary[i] == '0':
                res += '1'
            else:
                res += '0'
        
        return int(res, base=2)
        