# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lvl = [root]
        ans = []
        while lvl:
            ans.append([node.val for node in lvl])
            lvl = [c for x in lvl for c in (x.left,x.right) if c]
        return ans[::-1]
            
            
        
