"""
 dp思想， 每次遍历到当前房子， 记录当前房子如果使用三种颜色分别的价格
 """

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        f0, f1, f2 = 0, 0, 0
        for cost in costs:
            f0, f1, f2 = cost[0] + min(f1, f2), \
                            cost[1] + min(f0, f2), \
                                cost[2] + min(f0, f1)
        return min(f0, f1, f2)
