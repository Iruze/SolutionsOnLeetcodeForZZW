class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_S, stack_T = [], []
        for s in S:
            if s != '#': 
                stack_S.append(s)
            elif stack_S:
                stack_S.pop()
        for t in T:
            if t != '#':
                stack_T.append(t)
            elif stack_T:
                stack_T.pop()
        return stack_S == stack_T
