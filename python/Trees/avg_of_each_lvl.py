# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        ans = []
        
        def helper(root, lvl):
            if not root:
                return
            if len(ans) - 1 < lvl:
                ans.append([])
            ans[lvl].append(root.val)
            helper(root.left, lvl+1)
            helper(root.right, lvl+1)
        
        helper(root, 0)
        final = []
        for i in ans:
            final.append(float(sum(i))/len(i))
        return final
                
        
