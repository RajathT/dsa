# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

Trick : Check head-1 and head+1 with head
        """
        dummy = prev = cur = ListNode(None)
        
        while head:
            while head and ((head.val == prev.val) or (head.next and head.next.val == head.val)):
                prev = head
                head = head.next
            
            cur.next = head
            cur = cur.next
            
            if head:
                head = head.next  
            
        return dummy.next
                
        
