class Solution(object):
    def permute(self, nums):

        result = []

        def backtrack(start_index):
            if start_index == len(nums):
                result.append(nums[:])
                return

            for i in range(start_index, len(nums)):
                nums[start_index], nums[i] = nums[i], nums[start_index]
                backtrack(start_index + 1)
                nums[start_index], nums[i] = nums[i], nums[start_index]

        backtrack(0)

        return result
      
        
        
        