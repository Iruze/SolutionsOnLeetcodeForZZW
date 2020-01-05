# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        curr_deque = collections.deque()
        next_deque = collections.deque()
        curr_deque.append(root)
        res = []
        self.__bfs(root, curr_deque, next_deque, res)
        return res

    def __bfs(self, root, curr_deque, next_deque, res):
        while curr_deque:
            node = curr_deque.popleft()
            if node.left:
                next_deque.append(node.left)
            if node.right:
                next_deque.append(node.right)
            if not curr_deque:
                res.append(node.val)
                curr_deque = next_deque.copy()
                next_deque.clear()
    
