class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def helper(d, target):
            if target <= 0: return 0
            if d == 1: return +(f >= target)
            return sum(helper(d - 1, target - f0) for f0 in range(1, f + 1)) % MOD
        
        return helper(d, target)
        
