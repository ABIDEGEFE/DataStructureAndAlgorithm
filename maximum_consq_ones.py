class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        prev = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif count > prev:
                prev = count
                count = 0
            else:
                count = 0
        if count > prev:
            return count
        else:
            return prev

        
        