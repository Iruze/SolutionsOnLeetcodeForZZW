# 用堆，排序规则是欧几里得距离
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
