# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        def distance(x1, y1, x2, y2):
            dis = 0
            # (x1, y1)的层次比(x2, y2)的低，即深度更大
            while x1 > x2:
                x1, y1 = x1 - 1, y1 // 2
                dis += 1
            while x1 < x2:
                x2, y2 = x2 - 1, y2 // 2
                dis += 1
            # (x1, y1)和(x2, y2)上升直到找到共同的父节点
            while y1 != y2:
                y1 , y2 = y1 // 2, y2 // 2
                dis += 2
            return dis
        # bfs层次遍历找到k的位置，和所有叶子节点的位置
        queue = collections.deque([(0, 0, root)])
        x, y = 0, 0
        leaf = []
        while queue:
            layer, pos, node = queue.popleft()
            # 找到了k
            if node.val == k:
                x, y = layer, pos
            # 找到了叶子节点
            if not node.left and not node.right:
                leaf.append((layer, pos, node.val))
            # 下一层left, right节点入队
            if node.left:
                queue.append((layer + 1, pos * 2, node.left))
            if node.right:
                queue.append((layer + 1, pos * 2 + 1, node.right))
        return min(leaf, key=lambda p: distance(p[0], p[1], x, y))[-1]
