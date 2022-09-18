// 方法一： 前后指针
/ *
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    preNode, pNode := head, head
    for pNode != nil {
        if preNode.Val != pNode.Val {
            preNode.Next = pNode
            preNode = preNode.Next
        }
        pNode = pNode.Next
    }

    preNode.Next = pNode

    return head
}


*/


// 方法二： 单指针
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil {
        return head
    }

    cur := head
    for cur.Next != nil {
        if cur.Val == cur.Next.Val {
            cur.Next = cur.Next.Next
        } else {
            cur = cur.Next
        }
    }

    return head
}
