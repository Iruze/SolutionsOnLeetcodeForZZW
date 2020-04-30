# 取石头大小的相反数，构造大顶堆，模拟碰撞过程

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [*map(lambda x: -x, stones)]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x == y:
                continue
            heapq.heappush(stones, x - y)
        return -stones[0] if stones else 0
