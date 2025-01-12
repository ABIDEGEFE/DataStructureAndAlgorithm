class Solution(object):
    def longestPalindrome(self, s):
        count = 0
        op = ""
        pal = ""

        while count < len(s):
            sbs = s[count:s.rfind(s[count])+1]

            for i in sbs:
                op += i
                if op[::-1] == op and len(op) > len(pal):
                    pal = op
            op = ""
            count += 1

        return pal
        