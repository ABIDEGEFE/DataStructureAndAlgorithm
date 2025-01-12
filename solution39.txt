class Solution(object):
    def combinationSum(self, candidates, target):
       
        res = [[] for i in range(target + 1)]

        for i in candidates:
            if i <= target:
                res[i].append([i])

            for j in range(i + 1, target + 1):
                if res[j - i]:
                    for comb in res[j - i]:
                        res[j].append(comb + [i])

        return res[target]
        