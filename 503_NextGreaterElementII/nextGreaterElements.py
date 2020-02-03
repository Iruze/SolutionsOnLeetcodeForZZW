class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1 for _ in range(n)]
        # 模拟nums加倍了，故循环2倍
        for i in range(2 * n):
            while stack and nums[stack[-1] % n] < nums[i % n]:
                res[stack.pop() % n] = nums[i % n]
            stack.append(i % n)
        return res
