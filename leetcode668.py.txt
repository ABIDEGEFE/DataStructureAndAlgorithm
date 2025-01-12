class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        
        if sum(nums) % k != 0:
            return False
            
        required_sum = sum(nums) // k
        total = [0] * k
        nums.sort(reverse=True)

        def helper(index):
            if len(nums) == index:
                return sum(total) // k == required_sum

            for i in range(k):
                if total[i] + nums[index] > required_sum:
                    continue
                total[i] += nums[index]
                if helper(index + 1):
                    return True
                total[i] -= nums[index]

                if total[i] == 0:
                    break

            return False

        return helper(0)
        