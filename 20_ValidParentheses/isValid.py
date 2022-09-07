class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, c in enumerate(s):
            if not stack or c in {'(', '[', '{'}:
                stack.append(c)
            elif stack[-1] + c in {'()', '[]', '{}'}:
                stack.pop()
            else:
                return False
        return not stack
