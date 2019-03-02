# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

        """
        currDummyHead = l1
        
        carry = 0
    
        while l2 is not None:
            
            sum = l1.val + l2.val + carry
            l1.val = sum % 10
            carry = sum // 10
            
            if l1.next is None:
                l1.next = l2.next
                break
            if l2.next is None:
                break

            l1 = l1.next
            l2 = l2.next
            
        while carry > 0: 
            if l1.next is None:
                l1.next = ListNode(0)
                
            l1 = l1.next
            
            sum = carry + l1.val
            l1.val = sum % 10
            carry = sum // 10

        return currDummyHead
