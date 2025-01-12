class Solution(object):
    def groupAnagrams(self, strs):
        
        x = "".join(sorted(strs[0]))
        d = {x: [strs[0]]}
        
        for i in range(1, len(strs)):
            org = sorted(strs[i])
            x = "".join(org)
            if x in d:
                d[x].append(strs[i])
            else:
                d[x] = [strs[i]]

        res = []
        for ana in d.values():
            res.append(ana)

        return res
        