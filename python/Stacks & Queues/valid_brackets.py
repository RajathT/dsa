class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
Input: "([)]"
Output: false

Input: "{[]}"
Output: true
        """
        d = {'(':')','{':'}','[':']'}
        stack = []
        for i in list(s):
            if i in d:
                stack.append(i)
            else:
                if len(stack):
                    if d[stack.pop()] != i:
                        return False
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
