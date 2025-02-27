class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        container = {}

        for i in range(len(nums)):

            if nums[i] in container and i <= k + container[nums[i]]:
                return True
            container[nums[i]] = i

        return False

        
        

        