class Solution(object):
    def findDuplicates(self, nums):
        
        count = 0
        while count < len(nums):
            correctPos = nums[count]-1

            if correctPos < len(nums) and nums[count] != nums[correctPos]:
                nums[count], nums[correctPos] = nums[correctPos], nums[count]
            else:
                count += 1

        ans = []
        for i in range(len(nums)):
            if i != nums[i]-1:
                ans.append(nums[i])
        return ans
        