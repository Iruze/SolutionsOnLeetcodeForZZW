class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 0
        x_end = float('-Inf')
        for point in points:
            if point[0] > x_end:
                x_end = point[1]
                count += 1
        return count
