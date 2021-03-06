'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first():
            i, j, ans = 0, len(nums)-1, -1
            while i<=j:
                mid = (i+j)//2
                if nums[mid] == target:
                    ans = mid
                if nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1
            return ans
        
        def last():
            i, j, ans = 0, len(nums)-1, -1
            while i<=j:
                mid = (i+j)//2
                if nums[mid] == target:
                    ans = mid
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid - 1
            return ans
        
        return [first(), last()]
                    
                
                
                    
                    
        
