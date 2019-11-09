class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums)
        while start < end:
            mid = (start + end) // 2
            countLeft = sum(1 for num in nums if num >= start and num <= mid)
            if countLeft > mid - start + 1:
                end = mid
            else:
                start = mid + 1
        return start
