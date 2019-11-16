class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        d = [nums[i] - nums[i + 1] for i in range(n - 1)]
        count, last = 1, 0
        for e in d:
            if e == 0 or last * e > 0:
                continue
            if last == 0 or last * e < 0:
                last = e
                count += 1
        return count
