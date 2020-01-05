# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict()
        deque = collections.deque()
        deque.append((root, 0))
        max_depth = -1
        while deque:
            node, depth = deque.popleft()
            if node:
                max_depth = max(max_depth, depth)
                rightmost_value_at_depth[depth] = node.val 
                deque.append((node.left, depth + 1))
                deque.append((node.right, depth + 1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]
