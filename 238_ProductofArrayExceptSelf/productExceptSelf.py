class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        ans = [0] * n 
        tmp = 1
        for i in range(n):
            ans[i] = tmp
            tmp = nums[i] * tmp
        tmp = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= tmp
            tmp = nums[i] * tmp
        return ans
