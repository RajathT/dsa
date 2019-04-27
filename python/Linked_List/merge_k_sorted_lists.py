"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = new = ListNode(0)
        heap = []
        
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, l))
        while heap:
            val, l = heapq.heappop(heap)
            new.next = ListNode(val)
            new = new.next
            if l.next:
                heapq.heappush(heap, (l.next.val, l.next))
        
        return head.next
        
        
        
