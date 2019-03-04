class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
        """
        if len(nums) < 1:
            return None
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l)/2
            if m - 1 < l or m + 1 > r:
                break
            #If the index is divisible by 2, i.e. 3,3,7,10,10 it is odd so compare m == m+1. If ok l = m+2 else r=m 3,3,7,7,10
            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    l = m + 2
                else:
                    r = m
            #If the index is not divisible by 2, i.e. 1,1,2 it is odd so compare m == m-1. If ok l = m+1 else r=m 1,2,2
            else:
                if nums[m] == nums[m-1]:
                    l = m + 1
                else:
                    r = m
        return nums[l]
