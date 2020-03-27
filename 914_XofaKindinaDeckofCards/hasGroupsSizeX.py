class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # 求出deck所有数出现的次数，由次数组成的数组
        times = dict(Counter(deck)).values()
        # 最小的次数
        small = min(times)
        if small < 2: return False
        # 求最小次数的所有公约数组成的数组
        factor = [small]
        for i in range(2, math.floor(small) + 1):
            if small % i == 0:
                factor.append(i)
        # 拿每个small的公约数对times扫描
        # 也可以拿 2~small 对times扫描
        for f in factor:
            for t in times:
                if t % f != 0:
                    break
            # 如果有一个公约数能够整除全部的times
            else:
                return True
        return False
