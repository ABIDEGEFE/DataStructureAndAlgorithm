class Solution(object):
    def lengthOfLIS(self, nums):

        res = [1] * len(nums)
        for num in range(1, len(nums)):
            for j in range(0, num):
                if nums[j] < nums[num]:
                    res[num] = max(res[num], res[j] + 1)
            
        return max(res)

        