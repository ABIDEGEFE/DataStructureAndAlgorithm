# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        def helper(root, diff):
            if not root:
                return 0
            
            l = helper(root.left, diff)
            r = helper(root.right, diff)

            diff.append(abs(l-r))

            return (l+r)+root.val
        diff = []
        helper(root, diff)
        return sum(diff)


       
        