"""
按照起点逆序排列(position, speed)；
计算各车到达目的地用时，后车用时小于或等于前车的可以组成车队， 找到逆序组，即是车队数量：
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        sp = [*zip(position, speed)]
        # 按照起点倒序排列
        sp.sort(key=lambda x: x[0], reverse=True)
        # 计算各车到达目的地用时，后车用时小于或等于前车的可以组成车队
        time = [(target - x[0]) / x[1] for x in sp]
        # 找到逆序组，即是车队数量
        for i in range(len(time)):
            if time[i] != float('Inf'):
                ans += 1
                for j in range(i + 1, len(time)):
                    # 如果j车能够追上i车
                    if time[j] <= time[i]:
                        time[j] = float('Inf')
        return ans
