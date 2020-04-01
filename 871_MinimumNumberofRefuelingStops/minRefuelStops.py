# 方法一： 贪心-堆
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        ans = pre = 0
        tank = startFuel
        pq = []                         # 模拟最大堆，存入 <-当前站的油量>
        stations.append([target, float('Inf')])
        for loc, cap in stations:
            tank -= loc - pre           # 经过站时，油消耗剩余
            while pq and tank < 0:
                tank += -heappop(pq)    # 贪心法，加入最多的站的油
                ans += 1
            if tank < 0: return -1
            heappush(pq, -cap)          # 将站的油入堆
            pre = loc
        return ans
        
# 方法二：动态规划
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target: return 0
        n = len(stations)
        # dp[i][j]表示经过第i个站，第[j]次加油后能够行使的最远距离
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        # 第 i 个站，一次油都没有加，则还是原来的startFuel
        for i in range(n + 1):
            dp[i][0] = startFuel
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                # 1. 当前站不加油，则dp[i][j]等于前一个站的dp[i - 1][j]
                if dp[i - 1][j] >= stations[i - 1][0]:
                    dp[i][j] = dp[i - 1][j]
                # 2. 当前站加油，
                if dp[i - 1][j - 1] >= stations[i - 1][0]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + stations[i - 1][1])
        # 从加1~n次油检索，经过完n个加油站且最大行使路程大于target的
        for i in range(1, n + 1):
            if dp[n][i] >= target:
                return i
        return -1
