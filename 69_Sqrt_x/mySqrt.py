class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left, right = 1, x
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 == x or right - left == 1: return mid
            elif mid ** 2 < x: left = mid
            else: right = mid
        return left
