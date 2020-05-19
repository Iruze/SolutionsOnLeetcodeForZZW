class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        if not groupSizes:
            return []
        # size, ID 入堆
        hp = []
        for ID, size in enumerate(groupSizes):
            heapq.heappush(hp, [size, ID])
        
        ans = []
        # 从最小的size开始
        while hp:
            size = hp[0][0]
            tmp = []
            # 相同size的ID用tmp装在一起(贪心思想)
            for _ in range(size):
                tmp.append(heapq.heappop(hp)[1])
            ans.append(tmp)
        return ans
