"""
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin, end, m, c, D = 0, 0, 0, 0, {}
        
        while end < len(s):
            if s[end] not in D or D[s[end]] == 0:
                D[s[end]] = 1
            else:
                D[s[end]] += 1
                c = 1
            end += 1
            
            while c:
                if D[s[begin]] > 1:
                    c -= 1
                D[s[begin]] -= 1
                begin += 1
                
            m = max(m, end-begin)//Keeps increasing even before entering while loop

        return m
                
                
                
            
    
    
        
    
            
