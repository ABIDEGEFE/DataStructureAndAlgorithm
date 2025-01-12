class Solution(object):
    def titleToNumber(self, columnTitle):
        ix = 0
        ls = []
        reverseValue = columnTitle[::-1]

        for i in reverseValue:
            res = (ord(i)-64) * (26**ix)
            ls.append(res)
            ix += 1

        return sum(ls)

        