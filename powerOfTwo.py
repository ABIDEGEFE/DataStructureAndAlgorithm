class Solution(object):
    def summaryRanges(self, nums):

        if not nums:
            return []

        range_list = [str(nums[0])]
        min = nums[0]

        for i in range(0, len(nums)-1, 1):
            if nums[i+1] - nums[i] == 1:
                range_list[len(range_list)-1] = str(min) + "->" + str(nums[i+1])
            else:
                range_list.append(str(nums[i+1]))
                min = nums[i+1]

        return range_list
       
        