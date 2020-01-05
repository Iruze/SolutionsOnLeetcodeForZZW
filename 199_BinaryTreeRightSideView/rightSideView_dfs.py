# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict()
        stack = [(root, 0)]

        max_depth = -1
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]
