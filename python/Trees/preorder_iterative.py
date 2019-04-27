# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        st = []
        res = []
        curr = root
        
        while curr!=None or len(st)!=0:
            while curr!=None:
                res.append(curr.val)
                st.append(curr)
                curr = curr.left
            temp = st.pop()
            curr = temp.right
        return res
        
