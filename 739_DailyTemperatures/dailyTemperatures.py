class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = []
        # 时间复杂度O(N), 空间复杂度O(N)
        for i, v in enumerate(T):
            # stack维护单调递减栈
            while stack and T[stack[-1]] < v:
                # 弹出当前温度坐标，并与下一个更大坐标作差
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
