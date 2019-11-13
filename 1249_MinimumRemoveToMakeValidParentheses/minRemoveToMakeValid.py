class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, output = [], ''
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                continue
            if s[i] == '(' or not stack:
                stack.append(i)
            elif s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
        for i in range(len(s)):
            if i not in stack:
                output += s[i]
        return output
