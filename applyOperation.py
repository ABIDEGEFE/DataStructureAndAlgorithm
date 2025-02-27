class Solution(object):
    def applyOperations(self, nums):
        
        ix = 0
        while ix < len(nums)-1:
            if nums[ix] == nums[ix+1]:
                nums[ix] *= 2
                nums[ix+1] = 0

            ix += 1
        ix = 0
        for i in nums:
            j = ix+1

            while i == 0 and j<len(nums):
                if i != nums[j]:
                    temp = i
                    nums[ix] = nums[j]
                    nums[j] = temp
                    break
                j += 1
            ix += 1
        return nums