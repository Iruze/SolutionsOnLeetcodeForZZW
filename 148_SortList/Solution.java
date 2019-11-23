/* *****************************************************
/*               solution1: 递归解法
/* *****************************************************
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null)
            return head;
        
        ListNode end = head;
        while(end.next != null)
            end = end.next;
        
        return sort(head, end);
    }
    
    private ListNode sort(ListNode head, ListNode end) {
        // base，递归结束条件
        if(head == end)
            return head;
        ListNode mid = head, midfast = head;
        
        // 不能是: midfast != null && midfast.next != null
        // 因为存在 head.next = end 的情况不符合
        // 所以直接终点认为是 end，直接直接使得 中点mid 偏向头节点
        // 对于 midfast = midfast.next.next 的连续前进两步的必须要满足：
        // midfast != end && midfast.next != end， 否则while不能结束，报错stackoverflow.
        while(midfast != end && midfast.next != end) {
            midfast = midfast.next.next;
            mid = mid.next;
        }
        
        ListNode vhead = mid.next;
        mid.next = null;
        
        ListNode head1 = sort(head, mid);
        ListNode head2 = sort(vhead, end);
        
        return merge(head1, head2);
    }
    
    private ListNode merge(ListNode head1, ListNode head2) {
        if(head1 == null) return head2;
        if(head2 == null) return head1;
        
        ListNode resHead = null;
        if(head1.val < head2.val) {
            resHead = head1;
            head1.next = merge(head1.next, head2);
        }
        else {
            resHead = head2;
            head2.next = merge(head1, head2.next);
        }
        
        return resHead;
    }
}
