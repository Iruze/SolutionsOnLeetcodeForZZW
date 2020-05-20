# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # 分别记录当前层和下一层的节点
        cur, nxt = [root], []
        while cur:
            # ans作为预备的最后一层第一个节点
            ans = cur[0].val
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            # 下一层为空，说明cur已然是最后一层
            if not nxt:
                return ans
            cur, nxt = nxt, []
        return -1
