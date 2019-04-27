'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        D = collections.Counter(p)
        counter = len(set(p))
        begin, end, res = 0, 0, []
        while end < len(s):
            if s[end] in D:
                D[s[end]] -= 1
                if D[s[end]] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                if end-begin == len(p) : res.append(begin)
                if s[begin] in D:
                    D[s[begin]] += 1
                    if D[s[begin]] > 0:
                        counter += 1
                begin += 1
        return res
        
                    
        
                
            
            
        
        
            
            
        
