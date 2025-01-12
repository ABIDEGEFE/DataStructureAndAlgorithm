class Solution(object):
    def twoSum(self, numbers, target):
        
        left, right = 0, len(numbers)-1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return [left+1, right+1]
        