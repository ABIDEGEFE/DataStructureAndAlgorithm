class Solution(object):
    def majorityElement(self, nums):
        
        value = len(nums)/2

        for i in nums:
            count = nums.count(i)

            if count > value:
                return i

        
        