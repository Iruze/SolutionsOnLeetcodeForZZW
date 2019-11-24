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
        if(lists == null) return null;
        ListNode res = null;
        for(int i = 0; i < lists.length; ++i)
            res = mergeTwoLists(res, lists[i]);
        
        return res;
    }
    
    private ListNode mergeTwoLists(ListNode head1, ListNode head2) {
        if(head1 == null) return head2;
        if(head2 == null) return head1;
        
        ListNode dummy = new ListNode(-1);
        ListNode pNode = dummy;
        while(head1 != null && head2 != null) {
            if(head1.val < head2.val) {
                pNode.next = head1;
                head1 = head1.next;
            }
            else {
                pNode.next = head2;
                head2 = head2.next;
            }
            
            pNode = pNode.next;
        }
        
        if(head1 != null)
            pNode.next = head1;
        if(head2 != null)
            pNode.next = head2;
        
        return dummy.next;
    }
}
