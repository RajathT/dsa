# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Use a stack!
        """
        stack = []
        curr = root
        
        while curr!=None || len(stack)!=0:
            while curr!=None:
                stack.append(curr)
                curr = curr.left
            temp = stack.pop()
            res.append(temp)
            curr = curr.right
        
        
