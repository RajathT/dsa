# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
class Solution(object):
    
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        lvl = [root]
        ans = []
        while lvl:
            if len(ans)%2:
                ans.append([x.val for x in lvl][::-1])
            else:
                ans.append([x.val for x in lvl])
            lvl = [child for x in lvl for child in (x.left, x.right) if child]
        return ans
            
        
        
        
