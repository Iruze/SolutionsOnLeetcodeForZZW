"""
python3, 先排序+后贪心，复杂度：排序O(nlogn) + 贪心O(n)
"""

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 按照左端点大小排序，左端点相同时，按照右端点大小排序
        clips.sort()
        # 上一个clip的结尾
        last_end = 0
        i = 0
        cnt = 0
        while i < len(clips):
            # 寻找下一个clip的结尾，一定要最大
            nxt_end = 0
            # 找到了，片段数+1
            if clips[i][0] <= last_end:
                cnt += 1
            tmp = i
            # 在能够衔接的片段中，找结尾最大的那个
            while i < len(clips) and clips[i][0] <= last_end:
                nxt_end = max(nxt_end, clips[i][1])
                i += 1
            # 索引i还是原地，说明找不到任何片段衔接
            if tmp == i:
                return -1
            # 提前到达T
            if nxt_end >= T:
                return cnt
            # 记录下下一个片段最大的结尾
            last_end = nxt_end
        return -1
