class Solution(object):
    def convert(self, s, numRows):

        pos = numRows-1
        if len(s) < numRows or numRows == 1:
            return s

        ls = [""]*numRows
        for i in range(numRows):
            ls[i] += s[i]
        isUp = None

        for i in range(numRows, len(s)):
            if pos == 0:
                isUp = False
            if pos == numRows-1:
                isUp = True
            if isUp:
                pos -= 1
            else:
                pos += 1
            ls[pos] += s[i]

        return "".join(ls)
        