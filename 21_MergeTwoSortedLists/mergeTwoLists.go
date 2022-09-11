/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    /* 解法一： 递归
    if list1 == nil {
        return list2
    }
    if list2 == nil {
        return list1
    }

    head := new(ListNode)
    // var head *ListNode
    if list1.Val < list2.Val {
        head = list1
        head.Next = mergeTwoLists(list1.Next, list2)
    } else {
        head = list2
        head.Next = mergeTwoLists(list1, list2.Next)
    }

    return head
    */

    // 解法二：迭代解法
    dummy := &ListNode{
        -1,
        nil,
    }

    node := dummy
    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            node.Next = list1
            list1 = list1.Next
        } else {
            node.Next = list2
            list2 = list2.Next
        }
        
        node = node.Next
    }

    if list1 == nil {
        node.Next = list2
    } else {
        node.Next = list1
    }

    return dummy.Next
}
