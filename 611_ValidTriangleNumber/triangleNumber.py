class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        cnt = 0
        n = len(nums)
        for small in range(n - 2):
            if nums[small] == 0: continue
            for mid in range(small + 1, n - 1):
                if nums[mid] == 0: continue
                twoSum = nums[small] + nums[mid]
                third = bisect.bisect_left(nums, twoSum, mid + 1, n)
                cnt += third - mid - 1
        return cnt
