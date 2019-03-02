# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
Write a program to find the node at which the intersection of two singly linked lists begins.
        """
        if not headA or not headB:
            return None
        
        temp = headA
        l1 = 0
        while temp.next != None:
            temp = temp.next
            l1 += 1
        temp = headB
        l2 = 0
        while temp.next != None:
            temp = temp.next
            l2 += 1
        
        if l1<l2:
            while l1 < l2:
                headB = headB.next
                l2 -= 1
        else:
            while l2 < l1:
                headA = headA.next
                l1 -= 1
                
        while headA != headB and headA!= None and headB!= None:
            headA = headA.next
            headB = headB.next
        
        if headA == headB and headA != None and headB!= None:
            return headA
        else:
            return None
            
        
        
        
            
        
