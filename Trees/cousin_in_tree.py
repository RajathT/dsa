# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
'''
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        ans1 = [-1,-1]
        ans2 = [-1,-1]
        
        def helper(root, parent, d):
            if not root:
                return
            if root.val == x:
                ans1[0], ans1[1] = parent, d
            if root.val == y:
                ans2[0], ans2[1] = parent, d
            helper(root.left, root, d+1)
            helper(root.right, root, d+1)
            
        helper(root, None, 0)
        
        if ans1 == None and ans2[0] == None or (ans1[0] != ans2[0] and ans1[1] == ans2[1]):
            return True
        return False
        
            
