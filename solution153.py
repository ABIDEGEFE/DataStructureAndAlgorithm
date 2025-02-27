class Solution(object):
    def findMin(self, nums):

        if nums[-1] >= nums[0]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid

        return nums[right]
       
       
        