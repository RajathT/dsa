class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Method 1: Iterative
        '''
        if not nums:
            return -1
        
        i, j = 0, len(nums)-1
        
        while i<=j:
            m = (i+j)//2
            if nums[m] != target:
                if nums[m]<target:
                    i = m + 1
                else:
                    j = m - 1
            else:
                return m
        
        return -1
        '''
        #Method 2: Recursive
        if not nums:
            return -1
        
        def helper(i, j, nums):
            if i>j:
                return -1
            m = (i+j)//2
            if nums[m] != target:
                if nums[m]<target:
                    return helper(m+1, j, nums)
                else:
                    return helper(i, m-1, nums)
            else:
                return m
            
        return helper(0,len(nums)-1,nums)
        
        
            
        
            
        
