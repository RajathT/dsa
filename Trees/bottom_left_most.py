# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
'''
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lvl = [root]
        
        while lvl:
            new_lvl = [child for x in lvl for child in (x.left, x.right) if child]
            if not new_lvl:
                return lvl[0].val
            lvl = new_lvl
        
        
