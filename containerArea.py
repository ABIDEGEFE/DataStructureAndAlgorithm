class Solution(object):
    def maxArea(self, height):

        maxArea = 0
        currentArea = 0
        left = 0
        right = len(height)-1

        while left < right:

            width = right-left
            currentArea = min(height[left], height[right])*width
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea



       

       