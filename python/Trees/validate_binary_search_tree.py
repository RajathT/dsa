# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(min_val, max_val, root):
            if not root:
                return True
            if min_val < root.val and root.val < max_val:
                l = helper(min_val, root.val, root.left)
                r = helper(root.val, max_val, root.right)
                return l and r
            else:
                return False
            
        return helper(float('-inf'), float('inf'), root)
        
