class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        lft_to_rht, rht_to_lft = [1] * n, [1] * n
        # 左右各一遍动态规划
        # 从左向右dp
        for i in range(1, n):
            # 高于左边
            if ratings[i] > ratings[i - 1]:
                lft_to_rht[i] = lft_to_rht[i - 1] + 1
        count = lft_to_rht[-1]
        # 从右向左dp, 顺便计算count
        for i in range(n - 2, -1, -1):
            # 高于右边
            if ratings[i] > ratings[i + 1]:
                rht_to_lft[i] = rht_to_lft[i + 1] + 1
            # 取左右中最大的数目
            count += max(lft_to_rht[i], rht_to_lft[i])
        return count
