"""
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.lstrip(' ')
        flag, num = 0, ''
        
        for i in range (len(s)):
            if (i==0 and (s[i] == '-' or s[i]=='+')) or s[i].isdigit():
                if i==0 and (s[i] == '-' or s[i]=='+'):
                    if s[i] == '-':
                        flag = 1
                else:
                    num += s[i]
            else:
                break
        
        if num:
            num = -int(num) if flag else int(num)
            if num >= -(2**31) and num <= 2**31 -1:
                return num
            else:
                if num < -(2**31):
                    return -(2**31)
                else:
                    return 2**31-1
        else:
            return 0
                    
                
        
