class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = collections.defaultdict(list)
        for cand in candidates:
            dp[cand] = [[cand]]
        for cand in candidates:
            for t in range(cand, target + 1):
                if t >= cand:
                    for x in dp[t - cand]:
                        # 避免重复, [2,2,3]和[2,3,2]是同一个
                        tmp = x[:]
                        tmp.append(cand)
                        tmp.sort()
                        # 如果dp[t]中之前不存在则加入
                        if tmp not in dp[t]:
                            dp[t].append(tmp)
        return dp[target]
