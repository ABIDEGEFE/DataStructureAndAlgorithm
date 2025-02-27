class Solution(object):
    def reverseStr(self, s, k):
        output = ""
        prev = 0
        l = 0
        fac = k
        while len(output) != len(s):
            ls = s[prev:k]
            left = 0
            right = len(ls)-1
            
            if l%2 == 0:
                ls = ls[::-1]

            output += ls
            prev = k
            k = k + fac
            l +=1
        return output