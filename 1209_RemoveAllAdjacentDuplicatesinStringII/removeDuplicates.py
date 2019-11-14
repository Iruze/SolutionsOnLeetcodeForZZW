class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        for s1 in s:
            if not stack or stack[-1][0] != s1:
                stack.append([s1, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        output = ''
        for s2 in stack:
            output += s2[0] * s2[1]
        return output
