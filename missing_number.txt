class Solution(object):
    def missingNumber(self, nums):

        count = 0
        while count < len(nums):
            correctPos = nums[count]

            if count != correctPos and correctPos < len(nums):
                nums[count], nums[correctPos] = nums[correctPos], nums[count]
            else:
                count += 1

        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
        
        