class Solution(object):
    def jump(self, nums):
        
        current_pos = no_jump = 0
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1

        while current_pos != len(nums) - 2:
            no_jump += 1
            prev_jump = 0
            k = current_pos + 1
            r = nums[current_pos] + current_pos
            while r > current_pos:
                next_jump = nums[r] + r
                if next_jump >= len(nums) - 1:
                    return no_jump + 1
                if next_jump > prev_jump:
                    prev_jump = next_jump
                    k = r

                r -= 1
            current_pos = k

        
        