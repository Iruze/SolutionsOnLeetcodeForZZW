class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        idx = self._partition(nums, start, end)
        # partition函数返回的是前idx个降序排列的最大数
        while start < end:
            if idx < k - 1:
                start = idx + 1
                idx = self._partition(nums, start, end)
            else:
                end = idx
                idx = self._partition(nums, start, end)
        return nums[k - 1]

    # partition函数的平均时间复杂度为O(N)
    def _partition(self, nums, start, end):
        idx = random.randint(start, end)
        nums[idx], nums[end] = nums[end], nums[idx]
        large = start - 1
        for idx in range(start, end):
            if nums[idx] > nums[end]:
                large += 1
                if large != idx:
                    nums[large], nums[idx] = nums[idx], nums[large]
        large += 1
        nums[large], nums[end] = nums[end], nums[large]
        return large
