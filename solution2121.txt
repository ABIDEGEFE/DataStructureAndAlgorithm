class Solution(object):
    def getDistances(self, arr):

      
        d = {}
        for ix, num in enumerate(arr):
            if num in d:
                d[num].append(ix)
            else:
                d[num] = [ix]
        res = [0]*len(arr)

        for val in d.values():

            prifix_sum = 0
            for i in range(1, len(val)):
                prifix_sum += (val[i] - val[i-1]) * i
                res[val[i]] = prifix_sum

            sufix_sum = 0
            for j in range(len(val)-2, -1, -1):
                sufix_sum += (val[j+1] - val[j]) * (len(val) - j - 1)
                res[val[j]] += sufix_sum

        return res
      
        