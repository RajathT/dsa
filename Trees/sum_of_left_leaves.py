# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        def helper(root):
            if not root:
                return
            if root.left and root.left.left is None and root.left.right is None:
                    ans.append(root.left.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return sum(ans)
                
        
