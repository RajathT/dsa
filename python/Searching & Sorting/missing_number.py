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
    
    # Method 2: XOR - A^A = 0
    '''
    x1 = a[0] 
    x2 = 1
      
    for i in range(1,n): 
        x1 = x1 ^ a[i] 
          
    for i in range(2,n+2): 
        x2 = x2^i 
      
    return x1 ^ x2 
    '''
