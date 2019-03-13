# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def helper(root,ans):
            if not root:
                return None
            l = helper(root.left,ans)
            r = helper(root.right,ans)
            if not l and not r:
                ans.append(root.val)
            return ans
        
        return helper(root1,[]) == helper(root2,[])
        
        
            
        
