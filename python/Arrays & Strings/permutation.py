'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        def helper(l, temp):
            if len(l) == len(nums):
                ans.append(list(l))
            else:
                for i,val in enumerate(temp):
                    l.append(val)
                    helper(l, temp[:i]+temp[i+1:])
                    l.pop()
        nums = sorted(nums)
        helper([], nums)
        return ans
            
            
                
        
