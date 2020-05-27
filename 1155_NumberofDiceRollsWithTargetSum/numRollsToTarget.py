class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        self.m = 10 ** 9 + 7

        from functools import lru_cache
        @lru_cache(None)
        def helper(d, f, target):
            if target <= 0: return 0
            if d == 1 and target <= f: return 1
            if d == 1 and target > f: return 0
            ans = 0
            for i in range(1, f + 1):
                ans += helper(d - 1, f, target - i)
            return ans % self.m
        
        return helper(d, f, target)
