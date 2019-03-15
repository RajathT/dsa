# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''if not root:
            return []
        ans = []
        
        def helper(root, ht):
            if not root:
                return
            if len(ans) <= ht:
                ans.append([])
                ans[ht].append(root.val)
            ans[ht][0] = max(root.val, ans[ht][0])
            helper(root.left, ht+1)
            helper(root.right, ht+1)
        
        helper(root, 0)
        return [x[0] for x in ans]'''
        if not root:
            return []
        ans = []
        lvl = [root]
        while lvl:
            ans.append(max([x.val for x in lvl]))
            lvl = [child for x in lvl for child in (x.left, x.right) if child]
        return ans
        
