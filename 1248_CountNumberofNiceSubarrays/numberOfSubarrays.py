class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        lo, hi = 0, 0
        ans = 0
        # window表示窗口内奇数的个数
        window = 0
        while hi < len(nums):
            if nums[hi] & 1 == 1:
                window += 1
            hi += 1

            if window == k:
                # 计算右边能够满足k个奇数的长度
                tmp = hi
                while hi < len(nums) and nums[hi] & 1 == 0:
                    hi += 1
                hi_len = hi - tmp + 1

                # 计算左边能够满足k个奇数的长度
                lo_len = 1
                while nums[lo] & 1 == 0:
                    lo += 1
                    lo_len += 1
                
                # 结果=左边长度 × 右边长度
                ans += lo_len * hi_len
                # 窗口左端收缩
                lo += 1
                window -= 1
        return ans
