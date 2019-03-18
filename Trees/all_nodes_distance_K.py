'''
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(root, parent = None):
            if not root:
                return
            root.parent = parent
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root)
        
        seen = {target}
        dq = collections.deque()
        dq.append((target, 0))
        
        while dq:
            if dq[0][1] == K:
                return [node.val for node,d in dq]
            node, ht = dq.popleft()
            for n in (node.left, node.right, node.parent):
                if n and n not in seen:
                    seen.add(n)
                    dq.append((n, ht+1))
        return []
            
            
            
            
            
        
