class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x:x[0]-x[1])
        NA = len(costs) // 2
        ans = 0
        for i in range(NA):
            ans += costs[i][0] + costs[i + NA][1]
        return ans
