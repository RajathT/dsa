# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
'''
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.m = 0
        
        def func(root):
            l, r = 0, 0
            if root.left:
                l = func(root.left)
                l = l+1 if root.val == root.left.val else 0
            if root.right:
                r = func(root.right)
                r = r+1 if root.val == root.right.val else 0
            self.m = max(self.m, r+l)
            return max(l,r)
        
        func(root)
        return self.m
            
        
