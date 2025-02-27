class Solution(object):
    def firstMissingPositive(self, nums):

        count = 0
        while count < len(nums):
            correctPos = nums[count]-1

            if nums[count] > 0 and nums[count] < len(nums) and nums[count] != nums[correctPos]:
                nums[count], nums[correctPos] = nums[correctPos], nums[count]
            else:
                count += 1

        for i in range(len(nums)):
            if i != nums[i]-1:
                return i+1

        return len(nums)+1