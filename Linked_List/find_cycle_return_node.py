# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.
        """
        if not head:
            return head
        slw, fst = head, head
        while fst and fst.next:
            slw, fst = slw.next, fst.next.next
            if slw == fst:
                break
        
        if fst is None or fst.next is None:
            return None
        
        slw = head
        while slw!=fst:
            slw, fst = slw.next, fst.next
        return slw
        
