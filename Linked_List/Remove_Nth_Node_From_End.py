# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
        """
        if head.next is None and n == 1:
            return head.next
        
        fast = slw = head
        while n>0:
            fast = fast.next
            n-=1
        
        if fast is None:
            head = head.next
            return head
        
        while fast.next != None:
            slw, fast = slw.next, fast.next
        
        slw.next = slw.next.next
        
        return head
        
