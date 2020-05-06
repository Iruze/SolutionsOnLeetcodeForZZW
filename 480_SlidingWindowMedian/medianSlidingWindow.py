class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo, hi = 0, 0
        ans = []
        window = []
        # 套用 sliding window 模板
        while hi < len(nums):
            # 第一步，入窗就完事了
            bisect.insort_left(window, nums[hi])
            # 第二步，维护窗口，该出窗得出窗
            while len(window) > k:
                # 出窗
                window.pop(bisect.bisect_left(window, nums[lo]))
                # 窗口左端收缩
                lo += 1
            # 第三步，做该做的事
            if len(window) == k:
                # 注意这个求中位数的表达式，无论len(window)奇偶都如此
                ans.append((window[k // 2] + window[(k - 1) // 2]) / 2)
            # 最后，窗口右端始终右移，在路上
            hi += 1
        return ans
