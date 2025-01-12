class Solution(object):
    def fourSum(self, nums, target):

        sum_of_target = []
        nums = sorted(nums)

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, len(nums)-1
                while l < r:
                    if l > j + 1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    if r < len(nums)-1 and nums[r] == nums[r + 1]:
                        r -= 1
                        continue
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                    
                        sum_of_target.append([nums[l], nums[r], nums[j], nums[i]])
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1

        return sum_of_target
    
        