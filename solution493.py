class Solution(object):
    def reversePairs(self, nums):

        if len(nums) <= 1:
            return 0
        mid = len(nums)//2
        
        L = nums[:mid]
        R = nums[mid:]

        count = self.reversePairs(L) + self.reversePairs(R)
        
        j = i = 0
        L = sorted(L)
        R = sorted(R)

        while i < len(L) and j < len(R):

            if L[i] > 2*R[j]:
                # print("hey")
                count += len(L[i:])
                j += 1
            else:
                i += 1

        nums = L + R
        
        return count
        