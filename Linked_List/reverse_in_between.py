# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
        """
        if not head or head.next is None:
            return head
        
        prev = None
        curr = head
        
        prv = None
        nxt = None
        
        c = 1
        while curr != None:
            temp = prev
            if c == m:
                temp2 = curr
                while c <= n:
                    nxt = curr.next
                    curr.next = prv
                    prv = curr
                    curr = nxt
                    c+=1
                temp2.next = nxt
                if temp:
                    temp.next = prv
                else:
                    return prv
                return head
            else:
                prev = curr
                curr = curr.next
                c+=1
                
        
