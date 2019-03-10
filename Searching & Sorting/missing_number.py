class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

        """
        
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
