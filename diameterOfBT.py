# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = [0]
        def helper(root, diameter):
            if not root:
                return 0

            l = helper(root.left, diameter)
            r = helper(root.right, diameter)
            
            diameter[0] = max(diameter[0], l + r)
            return max(l, r) + 1
        
        helper(root, diameter)
        return diameter[0]
        
        