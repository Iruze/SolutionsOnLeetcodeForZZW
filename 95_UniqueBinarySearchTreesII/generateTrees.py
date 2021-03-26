# 记忆化递归



class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        @functools.lru_cache(None)
        # 注意: 这里是闭区间 [start, end]
        def helper(start, end):
            tree = list()
            if start > end:
                tree.append(None)
            # 根节点
            for val in range(start, end + 1):
                # 左子树搜索
                for lo in helper(start, val - 1):
                    # 右子树搜索
                    for hi in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left, root.right = lo, hi
                        tree.append(root)
            return tree
        
        return helper(1, n)
