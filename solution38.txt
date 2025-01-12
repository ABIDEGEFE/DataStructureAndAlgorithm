class Solution(object):
    def countAndSay(self, n):
       
        def helper(n):

            if n == 1:
                return "1"
            rle = helper(n-1)
            res = ""
            d = {}

            prev = key = rle[0]

            for i in rle:
                d[i] = d.get(i, 0) + 1

                if prev != i:
                    res += str(d[prev]) + prev
                    d[prev] = 0
                    prev = i
                key = i
        
            res += str(d[key]) + key
            return res
        
        return helper(n)
        