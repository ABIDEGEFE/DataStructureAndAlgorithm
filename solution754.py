class Solution(object):
    def pivotIndex(self, nums):

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):

            if total_sum - (left_sum*2) - nums[i] == 0:
                return i
            left_sum += nums[i]

        return -1
        