"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        def ht(root):
            if not root:
                return 0
            m = 0
            if root.children:
                for child in root.children:
                    m = max(m, ht(child))
            return 1 + m
    
        return ht(root)
        
