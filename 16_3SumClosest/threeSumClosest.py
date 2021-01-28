class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        nearest = 10 ** 7

        for i in range(n - 2):
            lo, hi = i + 1, n - 1
            # 双指针
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total == target:
                    return total
                elif total < target:
                    lo += 1
                else:
                    hi -= 1
                # 直接根据"最近"的定义取结果
                nearest = min(nearest, total, key=lambda x: abs(x - target))
        
        return nearest
