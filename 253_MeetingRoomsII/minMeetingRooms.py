class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        stack = []
        intervals.sort()
        for interval in intervals:
            if not stack or interval[0] < stack[-1]:
                stack.append(interval[1])
            else:
                stack[-1] = interval[1]
            stack.sort(reverse=True)
        return len(stack)
