class Solution(object):
    def frequencySort(self, s):
        
        d = {}
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1

        ls = []
        for key, val in d.items():
            ls.append((val, key))

        outP = ""
        for fr, str in sorted(ls, reverse=True):
            outP += fr*str

        return outP
        