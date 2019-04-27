# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''
import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dq = collections.deque()
        dq.append([root,1])
        
        while dq:
            temp,d = dq.popleft()
            if not temp.left and not temp.right:
                return d
            for child in (temp.left, temp.right):
                if child:
                    dq.append([child, d+1])
            
        
            
        
        
