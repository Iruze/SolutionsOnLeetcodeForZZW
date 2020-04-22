class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # 排序，保证结果是最早的时间
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        # 双指针移动，
        p1, p2 = 0, 0
        while p1 < len(slots1) and p2 < len(slots2):
            if slots1[p1][1] <= slots2[p2][0]:
                p1 += 1
            elif slots1[p1][0] >= slots2[p2][1]:
                p2 += 1
            else:
                start = max(slots1[p1][0], slots2[p2][0])
                end = min(slots1[p1][1], slots2[p2][1])
                # 符合的时间间隔
                if start + duration <= end:
                    return [start, start + duration]
                if slots1[p1][1] < slots2[p2][1]:
                    p1 += 1
                else:
                    p2 += 1
        return []
