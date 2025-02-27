class Solution(object):
    def findKthLargest(self, nums, k):

        n = len(nums) // 2 - 1
        for i in range(n, -1, -1):
            self.heapify(nums, len(nums), i)

        j = len(nums) - 1
        l = k
        while k > 0 and j >= 0:
            nums[j], nums[0] = nums[0], nums[j]
            self.heapify(nums, j, 0)
            j -= 1
            k -= 1

        return nums[len(nums) - l]

    def heapify(self, nums, n, i):

        parent_node = i
        first_child = 2 * i + 1
        second_child = 2 * i + 2

        if first_child < n and nums[first_child] > nums[parent_node]:
            parent_node = first_child
        if second_child < n and nums[second_child] > nums[parent_node]:
            parent_node = second_child

        if parent_node != i:
            nums[parent_node], nums[i] = nums[i], nums[parent_node]
            self.heapify(nums, n, parent_node)
        
        
         
        