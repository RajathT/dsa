'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = 1 , 0
        size = len(A)
        
        while odd < size and even < size:
            while odd < size and A[odd] % 2 == 1: 
                odd += 2
            while even < size and A[even] % 2 == 0: 
                even += 2
            if odd < size and even < size:
                A[odd], A[even] = A[even], A[odd]
                odd += 2 ; even += 2  # Optional Line
        return A
            
                
        
