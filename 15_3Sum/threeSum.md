class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # 1. 排序
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if nums[i] > 0:
                return ans
            # 1.1 外去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, n - 1
            # 2. 双指针
            while lo < hi:
                if nums[lo] + nums[hi] == -nums[i]:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    # 2.1 内去重
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < -nums[i]:
                    lo += 1
                else:
                    hi -= 1
        return ans
