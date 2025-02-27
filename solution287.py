class Solution(object):
    def findDuplicate(self, nums):
      
        count = 0
        while count < len(nums):
            correctPos = nums[count]-1

            if count != correctPos and correctPos < len(nums) and nums[count] != nums[correctPos]:
                nums[count], nums[correctPos] = nums[correctPos], nums[count]
            else:
                count += 1


        for i in range(len(nums)):
            if i != nums[i]-1:
                return nums[i]
        