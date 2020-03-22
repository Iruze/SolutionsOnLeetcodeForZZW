class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if not nums: return 0
            f, f1, f2 = 0, 0, 0
            for num in nums:
                f = max(f1 + num, f2)
                f1, f2 = f2, f 
            return f 
        if not nums: return 0
        return max(nums[0] + helper(nums[2:-1]), helper(nums[1:]))
