# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        max_num = max(nums)
        idx_max = nums.index(max_num)
        left_nums = nums[:idx_max][:]
        right_nums = nums[idx_max + 1:][:]
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)
        return root
