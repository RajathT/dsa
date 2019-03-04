class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
        """
        d = {}
        for i,val in enumerate(numbers):
            if val in d:
                return sorted([i+1,d[val]])
            d[target-val] = i+1
        
