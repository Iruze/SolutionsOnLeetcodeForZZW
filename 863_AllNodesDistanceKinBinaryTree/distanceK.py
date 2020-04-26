# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # 从target始往其下的左右子树搜索
        def searchChildren(tar_node, K):
            if not tar_node: return
            if K == 0: ans.append(tar_node.val)
            searchChildren(tar_node.left, K - 1)
            searchChildren(tar_node.right, K - 1)
        # dfs从root始往下遍历
        def dfs(root):
            if not root: return -1
            # base case，找到target节点
            if root.val == target.val:
                searchChildren(root, K)
                return K
            # 分别从左右子树找target
            l = dfs(root.left)
            r = dfs(root.right)
            # target不存在
            if l < 0 and r < 0:
                return -1
            # 因为只有一个target，此时存在于左子树
            elif l > 0:
                # 是左子树第一个节点
                if l == 1: ans.append(root.val)
                # K > 1，则必然存在于右子树
                # 将 K - 1(即l - 1)处理，等价于当前的root是target
                else: searchChildren(root.right, l - 2)
                return l - 1
            # 存在于右子树
            else:
                if r == 1: ans.append(root.val)
                else: searchChildren(root.left, r - 2)
                return r - 1
        ans = []
        dfs(root)
        return ans
        
