"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:    return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for i in node.children:
                stack.append(i)
            
        return res[::-1]
            
            
        
        
