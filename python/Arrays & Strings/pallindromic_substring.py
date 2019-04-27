class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []

        def check(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans.append(s[i:j+1])
                i -= 1
                j += 1
                
        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        
        return len(ans)
        
