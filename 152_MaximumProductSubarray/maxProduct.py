class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax, imin = 1, 1
        maxU = float('-Inf')
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax, imin = max(imax * num, num), min(imin * num, num)
            maxU = max(maxU, imax)
        return maxU
