"""
判断一个二叉树是否合法：左面子树中最大值<当前节点的值<右边子树中的最小值
我们进行递归判断，为空节点时，返回float("inf"), float("-inf")，这样它的任何父节点都将合法
如果当前节点不满足约束条件，返回float("-inf"), float("inf")，这样它的任何父节点都将不合法

参考：https://leetcode-cn.com/problems/largest-bst-subtree/solution/python-by-jasss-17/
"""
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return float('Inf'), float('-Inf'), 0
            l_min, l_max, l = helper(root.left)
            r_min, r_max, r = helper(root.right)
            if l_max < root.val < r_min:
                return min(root.val, l_min), max(root.val, r_max),l + r + 1
            return float('-Inf'), float('Inf'), max(l, r)

        return helper(root)[2]
