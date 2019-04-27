# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

        """
        less = less_head = ListNode(0)
        greater = greater_head = ListNode(0)
        node = head
        
        while node:
            if node.val < x:
                less.next = node
                less = less.next
            else:
                greater.next = node
                greater = greater.next
            node = node.next
    
        greater.next = None
        
        less.next = greater_head.next
        return less_head.next
            
        
