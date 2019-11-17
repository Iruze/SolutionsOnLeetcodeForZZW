class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 到达第0层和第1层花费力气都是0
        # 楼顶在len(cost)，故是cost数组最后一个元素下一层len(cost)+1
        # 动态规划公式：f(n) = min{f(n-1)+cost[n-1], f(n-2)+cost[i-2]}
        f1, f2 = 0, 0
        for i in range(2, len(cost) + 1):
            f2, f1 = f1, min(f1 + cost[i - 1], f2 + cost[i - 2])
        return f1
