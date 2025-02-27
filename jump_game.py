class Solution(object):
    def canJump(self, nums):
        
        if nums[0] == 0 and len(nums) != 1:
            return False
        if nums[0] >= len(nums) - 1:
            return True
        current_pos = 0
        while current_pos < len(nums):

            r = nums[current_pos] + current_pos
            prev_jump = 0
            k = current_pos + 1
            max_ind = r
            while current_pos < r < len(nums):
                next_jump = nums[r] + r
                if next_jump >= len(nums) - 1:
                    return True
                if next_jump > prev_jump:
                    k = r
                    prev_jump = next_jump
                r -= 1

            if nums[max_ind] == 0 and prev_jump <= nums[max_ind] + max_ind:
                return False
            

        return True
        