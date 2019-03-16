"""
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        ans = []
        
        def backtrack(l, ind):
            ans.append(list(l))
            for i in range(ind, len(nums)):
                l.append(nums[i])
                backtrack(l, i+1)
                l.pop()
        
        backtrack([], 0)
        return ans
        '''
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res
        
        
                
