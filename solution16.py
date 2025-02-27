class Solution(object):
    def threeSumClosest(self, nums, target):

        variation = 10**8
        res = 0
        nums = sorted(nums)
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                x = target - total
                if x < 0:
                    x = -1*x
                if x < variation:
                    res = total
                    variation = x
                if total < target:
                    left += 1
                else:
                    right -= 1

        return res
  
        