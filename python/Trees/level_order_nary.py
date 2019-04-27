"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        ans = []
        while level:
            ans.append([n.val for n in level])
            level = [child for node in level for child in node.children if child]
        return ans
            
            
