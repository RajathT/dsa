class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        A = [0]*len(nums)
        
        for num in nums:
            A[num-1] = 1
        
        return [i+1 for i in range(len(nums)) if not A[i]]
