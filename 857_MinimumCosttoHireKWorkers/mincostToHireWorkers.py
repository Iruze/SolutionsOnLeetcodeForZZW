class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        """
        既要按比例分配薪资，又要满足最低薪资，则所有人的"薪劳比">=K个人中的某一个
        ，即，K个人中需要找到最低“薪劳比”ratio，其他K-1个人按照他的ratio分配工资
        ，如此就能达到工资组最少支付工资(贪心思想)
        1. ratio = wage[i] / quality[i]
        2. 最少支付工资和 = ratio * sum(k个人的quality)
        将N个ratio排序，从第k个人开始寻找（前k-1个人的ration已经入堆
        ，需要比较在剩下的K-N上长度为k的区间上的最小支付工资和）
        """
        N = len(quality)
        # 获取"薪劳比"升序排列
        orders = sorted(range(N), key=lambda k: wage[k] / quality[k])
        qua = []
        sumq = 0.
        ans = float('Inf')
        for idx in orders:
            # 建立quality的最大堆，随时准备弹出最大quality
            heapq.heappush(qua, -quality[idx])
            sumq += quality[idx]
            # 维护工资组人数为K
            if len(qua) > K:
                # quality相加的个数维持在k个，大于k时则去掉其中最大的一个quality，保持总和sumq最小
                sumq += heapq.heappop(qua)
            if len(qua) == K:
                # 比较所有的具有k长度区间的工资组
                ratio = wage[idx] / quality[idx]
                ans = min(ans, sumq * ratio)
        return ans
