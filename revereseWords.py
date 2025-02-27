class Solution(object):
    def reverseWords(self, s):
        ls = s.split()
        outPut = ""
        for i in ls:
            outPut += i[::-1] + " "
        return outPut.strip()
        