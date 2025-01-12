# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        path = {}
        mode = []
        def helper(root):
            if not root:
                return
            if root.val in path:
                path[root.val] = path.get(root.val, 0)+1
            else:
                path[root.val] = 1

            helper(root.left)
            helper(root.right)

            return path
        p = helper(root)
        max_val = max(p.values())

        for k, v in p.items():
            if v == max_val:
                mode.append(k)
        return mode


        
        