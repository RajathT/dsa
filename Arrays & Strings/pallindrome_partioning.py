'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        
        def backtrack(temp, start):
            if start == len(s):
                print(temp)
                ans.append(list(temp))
            else:
                for i in range(start, len(s)):
                    #print(start, i, s[start:i+1])
                    if s[start:i+1] == s[start:i+1][::-1]:
                        temp.append(s[start:i+1])
                        backtrack(temp, i+1)
                        temp.pop()
        
        backtrack([], 0)
        return ans
