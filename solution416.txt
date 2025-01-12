class Solution(object):
    def canPartition(self, nums):

        total = sum(nums)
        if total % 2 != 0:
            return False
        half_value = total // 2

        res = [False] * (half_value + 1)
        res[0] = True

        for i in nums:
            for j in range(half_value, i - 1, -1):
                if res[j - i]:
                    res[j] = True

        return res[-1]
        
        

        