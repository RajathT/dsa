"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.max_len, self.start = 0, 0
        
        def helper(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i -= 1
                j += 1
                
                if self.max_len < j-i-1:
                    self.max_len, self.start = j-i-1, i+1
                    
        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)
            
        return s[self.start: self.start+self.max_len]
        
