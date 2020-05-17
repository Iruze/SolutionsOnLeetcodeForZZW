class Solution:
    # newInterval 沿着 intervals 进行 cruise
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        ans = []
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        tmp = [newInterval[0], newInterval[1]]
        while i < n and intervals[i][0] <= newInterval[1]:
            tmp[0] = min(tmp[0], intervals[i][0])
            tmp[1] = max(tmp[1], intervals[i][1])
            i += 1
        ans.append(tmp)
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
