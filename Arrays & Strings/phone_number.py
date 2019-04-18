"""
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        num_pad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        temp = []
        for num in list(digits):
            temp.append(num_pad[num])
        
        res = []
        
        def helper(l, s):
            if not l:
                res.append(str(s))
                return
            
            for e in list(l[0]):
                helper(l[1:], s+e)
        
        helper(temp, '')
        
        return res
                
            
        
                
                
                
                
                
                
