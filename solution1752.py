class Solution(object):
    def check(self, nums):

        is_sorted = True
        first_item = nums[0]
        i = 1

        while i < len(nums):
            if nums[i] < nums[i-1]:
                if nums[i] > first_item:
                    return False
                j = i + 1
                while j < len(nums):

                   
                    if nums[j] < nums[j-1] or nums[j] > first_item:
                        is_sorted = False
                        break
                    j += 1

            i += 1
        return is_sorted
    
        