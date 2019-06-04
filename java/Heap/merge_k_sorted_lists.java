/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        PriorityQueue<ListNode> pq = new PriorityQueue<>(lists.length, new Comparator<ListNode>(){
            @Override
            public int compare(ListNode obj1, ListNode obj2){
                return obj1.val - obj2.val;
            }
        });
        
        for (ListNode temp: lists){
            if (temp!=null) pq.add(temp);
        }
        
        ListNode res = new ListNode(0);
        ListNode head = res;
        while(pq.size()!=0){
            ListNode temp = pq.poll();
            res.next = new ListNode(temp.val);
            res = res.next;
            if (temp.next!=null) pq.add(temp.next);
        }
        
        return head.next;
    }
}
