'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        
        while i<j:
            while i<j and A[i]%2 == 0:
                i += 1
            while j>i and A[j]%2 == 1:
                j -= 1
            if i<j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        return A
        
