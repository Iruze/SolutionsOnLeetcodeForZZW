class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # 将十进制的节点刻画成dict的树
        tree = dict()
        # 索引是(d, p)
        for num in nums:
            num_str = str(num)
            d, p, v = int(num_str[0]), int(num_str[1]), int(num_str[2])
            tree[(d, p)] = v
        self.ans = 0

        def helper(root, tree, pre=0):
            if root not in tree: return 0
            l, r = (root[0] + 1, root[1] * 2 - 1), (root[0] + 1, root[1] * 2)
            if l not in tree and r not in tree:
                self.ans += pre + tree[root]
                return
            # 分别找左右路径
            helper(l, tree, pre + tree[root])
            helper(r, tree, pre + tree[root])
        
        helper((1, 1), tree)

        return self.ans
