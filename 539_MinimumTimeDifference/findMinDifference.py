"""
一天24*60分钟，所以：

1). 将给的时间转化为分钟;

2). 排序

因为是比较一个环的相邻最小差，所以最后还需要比较一下环首和环尾的差：

"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, v in enumerate(timePoints):
            h, m = v.split(':')
            timePoints[i] = int(h) *60 + int(m)
        
        timePoints.sort()
        ans = float('Inf')
        for i in range(1, len(timePoints)):
            ans = min(ans, timePoints[i] - timePoints[i - 1])
        return min(ans, 24 * 60 + timePoints[0] - timePoints[-1])
