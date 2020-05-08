class Solution:
    def canCross(self, stones: List[int]) -> bool:

        end = stones[-1]
        s = set(stones)

        from functools import lru_cache

        # 记忆化搜索
        @lru_cache(None)
        def helper(start, jump):
            # base case
            if start == end:
                return True
            # 当前3中跳法
            for j in (jump - 1, jump, jump + 1):
                if j <= 0: continue
                if start + j in s and helper(start + j, j):
                    return True
            return False
        
        return helper(0, 0)
