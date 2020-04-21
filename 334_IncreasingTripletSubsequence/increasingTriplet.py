class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        small, mid = float('Inf'), float('Inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            elif num > mid:
                return True
        return False
