class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = [gas[i] - cost[i] for i in range(n)]
        if sum(tank) < 0:
            return -1
        start_position, cur_tank = 0, 0
        for i in range(n):
            cur_tank += tank[i]
            if cur_tank < 0:
                cur_tank = 0
                start_position = i + 1
        return start_position
