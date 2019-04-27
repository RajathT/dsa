# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            carry = 0
            head = new = ListNode(0)
            
            while l1 and l2:
                val = l1.val + l2.val
                new.next = ListNode((val + carry)%10)
                carry = (val + carry)//10
                l1, l2, new = l1.next, l2.next, new.next
            while l1:
                new.next = ListNode((l1.val + carry)%10)
                carry = (l1.val + carry)//10
                l1, new = l1.next, new.next
            while l2:
                new.next = ListNode((l2.val + carry)%10)
                carry = (l2.val + carry)//10
                l2, new = l2.next, new.next
            
            if carry:
                new.next = ListNode(carry)
            
            return head.next
