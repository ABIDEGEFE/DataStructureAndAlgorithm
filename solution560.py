class Solution(object):
    def subarraySum(self, nums, k):

        d = {0: 1}

        total = count = 0

        for i in nums:
            total += i
            if total - k in d:
                count += d[total - k]

            d[total] = d.get(total, 0) + 1

        return count