"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
        """
        if not head:
            return head
        
        def func(root):
            while True:
                if root.child != None:
                    new = func(root.child)
                    temp = root.next
                    root.child.prev = root
                    root.next = root.child
                    root.child = None
                    new.next = temp
                    if temp:
                        temp.prev = new
                        root = temp
                    else:
                        return new
                elif root.next:
                    root = root.next
                else:
                    return root
        root = head
        temp=func(root)
        return head
                    
        
