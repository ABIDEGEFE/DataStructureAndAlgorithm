class Solution(object):
    def subsetsWithDup(self, nums):

        res = []
        visisted = [False] * len(nums)
        nums.sort()

        def helper(start, comb):
            res.append(comb[:])
            if len(comb) == len(nums):
                return

            for i in range(start, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not visisted[i - 1]:
                    continue
                visisted[i] = True
                comb.append(nums[i])
                helper(i + 1, comb)

                comb.pop()
                visisted[i] = False

        helper(0, [])
        return res
        
        