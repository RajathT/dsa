# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
        """
        def helper(root):
            if not root:
                return None
            if root.val < L:
                return helper(root.right)
            elif root.val > R:
                return helper(root.left)
            else:
                root.left = helper(root.left)
                root.right = helper(root.right)
                return root
        return helper(root)
        
