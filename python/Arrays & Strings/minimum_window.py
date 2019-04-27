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
        D = collections.Counter(T)
        counter = len(set(T))
        begin, end, m, ans = 0, 0, float('inf'), ''
        
        while end < len(S):
            if S[end] in D:
                D[S[end]]-=1
                if not D[S[end]]:
                    counter -= 1
            end += 1
            while not counter:
                if end - begin < m:
                    m = end - begin
                    ans = S[begin:end]
                if S[begin] in D:
                    D[S[begin]]+=1
                    if D[S[begin]]>0:
                        counter += 1
                begin += 1
        return ans
        
            
            
                
        
        
