'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        def helper(l, temp):
            if len(l) == len(nums):
                ans.append(list(l))
            else:
                for i in range(len(temp)):
                    if i>0 and temp[i] == temp[i-1]:continue
                    l.append(temp[i])
                    helper(l, temp[:i]+temp[i+1:])
                    l.pop()
        nums = sorted(nums)
        helper([], nums)
        return ans
        
