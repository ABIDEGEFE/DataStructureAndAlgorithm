# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        res = []
        def helper(root):
            if not root:
                return 
            res.append(root.val)

            helper(root.left)
            helper(root.right)

            return res
        res = sorted(helper(root), reverse=True)
        
        minm = 100000
        for i in range(len(res)-1):
            if abs(res[i+1]-res[i]) < minm:
                minm = abs(res[i+1]-res[i])
        return minm

      
        
        
        