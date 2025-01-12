class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        def mergeSort(nums):

            if len(nums) <= 1:
                return

            mid = len(nums)//2
            left_arr = nums[:mid]
            right_arr = nums[mid:]

            mergeSort(left_arr)
            mergeSort(right_arr)

            i = j = k = 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    nums[k] = left_arr[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right_arr[j]
                    j += 1
                    k += 1

            while i < len(left_arr):
                nums[k] = left_arr[i]
                i += 1
                k += 1
            while j < len(right_arr):
                nums[k] = right_arr[j]
                j += 1
                k += 1
            return nums
        return mergeSort(nums)