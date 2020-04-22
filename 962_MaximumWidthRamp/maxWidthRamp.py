class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        ans = 0
        # 最大宽度的左端必然在stack中
        for i, v in enumerate(A):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        
        for i in range(len(A) - 1, -1, -1):
            # 一定要带上=，在=时要弹出值
            while stack and A[i] >= A[stack[-1]]:
                ans = max(ans, i - stack.pop())
        return ans
