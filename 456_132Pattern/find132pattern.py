class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        second = float('-Inf')
        for num in nums[::-1]:
            if num < second:                          # third < second, 返回true
                return True
            while stack and num > stack[-1]:          # 始终保持second是最大的"second",以便快速找到third
                second = max(second, stack.pop())
            stack.append(num)
        return False
