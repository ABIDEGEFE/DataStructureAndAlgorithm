class Solution(object):
    def topKFrequent(self, nums, k):
       
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        val_key = []
        for key, val in d.items():
            val_key.append((val, key))
        val_key = sorted(val_key)

        i = len(val_key) - 1
        res = []

        while k > 0:
            res.append(val_key[i][-1])
            i -= 1
            k -= 1

        return res
        