# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法一: O(logn * logn)
# 每一层里面都需要求一次高度,单次求高度时间为O(logn), 所以总的时间复杂度为 O(logn * logn)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.__countLevel(root.left)
        right = self.__countLevel(root.right)
        if left == right:
            return self.countNodes(root.right) + (1 << left)
        else:
            return self.countNodes(root.left) + (1 << right)

    def __countLevel(self, root):
        level = 0
        while root:
            level += 1
            root = root.left
        return level

    
# 解法二: O(n)
# 后序遍历, 每一个节点遍历一次, 缺点:　没有利用到＂完全二叉树＂的性质
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
