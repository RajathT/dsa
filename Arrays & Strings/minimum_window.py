import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
        """
        i, j = 0, 0
        counter = len(set(t))
        ans = ''
        D = collections.Counter(t)
        m = len(s)+1
        while j < len(s):
            
            if s[j] in D:
                D[s[j]] -= 1
                if D[s[j]] == 0:
                    counter -= 1
            j += 1
            
            while counter == 0:
                if j-i < m:
                    m = j-i
                    ans = s[i:j] 
                if s[i] in D:
                    D[s[i]] += 1
                    if D[s[i]] > 0:
                        counter += 1
                i += 1
            
        return ans
        
            
            
                
        
        
