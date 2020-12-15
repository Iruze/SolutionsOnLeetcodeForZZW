# 解法一：
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
    
    
    
# 解法二： 堆排序（最优）
"""
堆排序，堆里面存储当前最早结束的会议的时间，和下一次会议的开始时间比较：

1). 如果新会议时间小于（先于）， 则会议冲突，当前会议需要重新开一个房间， 加入到rooms堆中去；
2). 反之， 如果大于（晚于），则新会议可以复用最早结束的会议的房间
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort()
        for interval in intervals:
            # 下一个会议开始时间小于当前最早结束会议时间，
            #  ，则下一个会议需要单独开一个房间
            if not rooms or rooms[0] > interval[0]:
                heapq.heappush(rooms, interval[1])
            else:
                # 此时，可以复用当前最早结束的会议的房间
                heapq.heapreplace(rooms, interval[1])
        return len(rooms)
