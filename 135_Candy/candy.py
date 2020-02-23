class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        lft_to_rht, rht_to_lft = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                lft_to_rht[i] = lft_to_rht[i - 1] + 1
        count = lft_to_rht[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                rht_to_lft[i] = rht_to_lft[i + 1] + 1
            count += max(lft_to_rht[i], rht_to_lft[i])
        return count
