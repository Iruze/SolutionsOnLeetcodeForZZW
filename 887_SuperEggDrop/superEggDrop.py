class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dfs(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]
            res = float('Inf')
            lo, hi = 1, N
            while lo <= hi:
                mid = lo + ((hi - lo) >> 1)
                broken = dfs(K - 1, mid - 1)
                full = dfs(K, N - mid)
                if broken > full:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, full + 1)
            memo[(K, N)] = res
            return res
        return dfs(K, N)
