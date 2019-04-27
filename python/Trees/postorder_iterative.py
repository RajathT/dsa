# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        st1, st2 = [], []
        
        st1.append(root)
        
        while len(st1)!=0:
            temp = st1.pop()
            st2.append(temp.val)
            if temp.left:
                st1.append(temp.left)
            if temp.right:
                st1.append(temp.right)
        
        return st2[::-1]
            
        
        
