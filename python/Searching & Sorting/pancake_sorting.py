'''
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
'''
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if sorted(A) == A:
            return []
        i = len(A)-1
        res = []
        while i>0:
            ind = A.index(max(A[:i+1]))
            if ind !=0:
                res.append(ind+1)
                A = A[:ind+1][::-1]+A[ind+1:]
            A = A[:i+1][::-1] + A[i+1:]
            res.append(i+1)
            i -= 1
        return res
            
            
            
            
        
