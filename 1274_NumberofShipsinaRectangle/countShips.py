# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1 = topRight.x, topRight.y
        x2, y2 = bottomLeft.x, bottomLeft.y

        if x1 < x2 or y1 < y2 or not sea.hasShips(topRight, bottomLeft):
            return 0
        if (x1, y1) == (x2, y2):
            return 1
        
        # 将给定的矩形中中间进行四分
        xmid = (x1 + x2) // 2
        ymid = (y1 + y2) // 2

        return self.countShips(sea, Point(xmid, ymid), Point(x2, y2)) + \
        self.countShips(sea, Point(x1, ymid), Point(xmid + 1, y2)) + \
        self.countShips(sea, Point(xmid, y1), Point(x2, ymid + 1)) + \
        self.countShips(sea, Point(x1, y1), Point(xmid + 1, ymid + 1))
