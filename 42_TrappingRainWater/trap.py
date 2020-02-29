# 解法一： 备忘录解法
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        n = len(height)
        l_max, r_max = [0] * n, [0] * n
        l_max[0], r_max[n - 1] = height[0], height[n - 1]
        # 找到左边最高的柱子
        for i in range(1, n):
            l_max[i] = max(l_max[i - 1], height[i])
        # 找到右边最高的柱子
        for i in range(n - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], height[i])
        # 综合左右，得到最终结果
        ans = 0
        # 注意是从 1 到 n - 2，因为两头不会盛水
        for i in range(1, n - 1):
            ans += min(l_max[i], r_max[i]) - height[i]
        return ans
        
        
# 解法二： 双指针解法
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        n = len(height)
        left, right = 0, n - 1
        ans = 0
        l_max, r_max = 0, 0
        while left <= right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1
        return ans
