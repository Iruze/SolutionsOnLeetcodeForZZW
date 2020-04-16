"""
第i天不出行，那么第i天可以什么也不干，也可以买任意一种票，但是最优解肯定是什么也不干，延续第i - 1天的花费。
第i天要出行，那么第i天必然要有票。表面上看取决于前几天是不是有7天票，30天票，但是到底取决于哪一天？
按照贪心原则，为了让当天的花费平均成本最低，那么7天票最好是就在7天前买的，30天票就是30天买的，还有一种就是当天直接买一张一天票。
这三个选择选个最小的值就是推导值，这也是转移方程的得来。
"""

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastday = days[-1]
        dp = [0] * (lastday + 1)
        for day in range(1, lastday + 1):
            if day not in days:
                dp[day] = dp[day - 1]
            else:
                dp_7 = 0 if day - 7 < 0 else dp[day - 7]
                dp_30 = 0 if day - 30 < 0 else dp[day - 30]
                dp[day] = min(
                    dp[day - 1] + costs[0], 
                    dp_7 + costs[1], 
                    dp_30 + costs[2]
                )
        return dp[-1]
        
