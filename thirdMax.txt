class Solution(object):
    def thirdMax(self, nums):
        nums = sorted(nums, reverse=True)
        count = 1
        prev = nums[0]

        for i in range(1, len(nums)):
            if prev > nums[i]:
                count += 1
            if count == 3:
                return nums[i]
            prev = nums[i]
            
        return nums[0]
        