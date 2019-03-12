# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
Input: [1,1,1,1,1,null,1]
Output: true
Input: [2,2,2,5,2]
Output: false
        """
        def helper(root):
            if not root:
                return True
            if root.left:
                if root.val != root.left.val:
                    return False
            if root.right:
                if root.val != root.right.val:
                    return False 
            return helper(root.left) and helper(root.right)
    
        return helper(root)
