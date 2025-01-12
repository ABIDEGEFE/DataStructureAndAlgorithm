class Solution(object):
    def searchRange(self, nums, target):

        def left_extreme(nums, target):

            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return l

        def right_exterme(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1

            return r

        first_index = left_extreme(nums, target)
        last_index = right_exterme(nums, target)

        if first_index >= len(nums) or nums[first_index] != target:
            return [-1, -1]
        
        return [first_index, last_index]
        