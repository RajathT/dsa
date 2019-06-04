/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode slow = head, fast = head;
        while (n!=0 && fast != null) {
            fast = fast.next; n--;
        }
        if (fast == null){
            head = head.next; return head;
        }
        while (fast.next != null){
            slow = slow.next; fast = fast.next;
        }
        slow.next = slow.next.next;
        
        return head;
        
    }
}
