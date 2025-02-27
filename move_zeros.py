class Solution(object):
    def moveZeroes(self, nums):

        current = 0
        next = 1

        while next < len(nums) and current < len(nums):
            if nums[current] == 0:
                nums[current], nums[next] = nums[next], nums[current]
            else:
                current += 1
            if nums[next] == 0 or current >= next:
                next += 1
      
        