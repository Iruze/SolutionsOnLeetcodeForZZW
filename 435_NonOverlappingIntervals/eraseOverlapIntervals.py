class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        x_end = float('-Inf')
        for interval in intervals:
            if x_end <= interval[0]:
                count += 1
                x_end = interval[1]
        return len(intervals) - count
