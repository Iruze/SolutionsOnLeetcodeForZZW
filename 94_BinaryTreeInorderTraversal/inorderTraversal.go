/**
解法一： 迭代

func inorderTraversal(root *TreeNode) []int {
    stack := []*TreeNode{}
    res := []int{}

    for len(stack) != 0 || root != nil {
        for root != nil {
            stack = append(stack, root)
            root = root.Left
        }

        root = stack[len(stack) - 1]
        // go的语法糖，root.Val 等价 (*root).Val
        // res = append(res, (*root).Val)
        res = append(res, root.Val)
        root = root.Right
        stack = stack[:len(stack) - 1]
    }

    return res
}

 */


/**
解法二：递归
*/
func inorderTraversal(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    left := inorderTraversal(root.Left)
    right := inorderTraversal(root.Right)
    return append(append(left, root.Val), right...)
}
