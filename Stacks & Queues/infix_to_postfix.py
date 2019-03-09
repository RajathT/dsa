#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:02:16 2019

@author: rajathtellapuram
"""

s = "a+b*(c^d-e)^(f+g*h)-i"

d = {'+':1,'-':1,'*':2,'/':2,'^':3,'(':4}

stack = []
ans = ''

for i in list(s):
    if i not in d and i != ')':
        print(i)
        ans += i
    else:
        if len(stack)!=0:
            if i != ')':
                while len(stack) and d[stack[len(stack)-1]] >= d[i]:
                    if stack[len(stack)-1] != '(':
                        ans += stack.pop()
                    else:
                        break
            else:
                while len(stack) and stack[len(stack)-1] != '(':
                    ans += stack.pop()
                stack.pop()
        
        if i != ')':
            stack.append(i)
        
print(ans + ''.join(stack[::-1]))

#abcd^e-fgh*+^*+i-
            
                    
        



