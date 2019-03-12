class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Example 1:

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
        i, j, c, dm = 0, 0, 0, 0
        d = {}
        while j<len(s):
            if s[j] not in d or d[s[j]] == 0:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
                c += 1
            j += 1
            while c > 0:
                if d[s[i]] > 1:
                    c -= 1
                d[s[i]] -= 1
                i += 1
            dm = max(dm, j-i)
            #print(dm , j, i)
        return dm
                
                
                
            
    
    
        
    
            
