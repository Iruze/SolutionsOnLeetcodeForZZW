class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for token in tokens:
            try:
                _ = int(token)
                ans.append(token)
            except:
                v1 = int(ans.pop())
                v2 = int(ans[-1])
                ans[-1] = self.cal(v2, v1, token)
        return int(ans[0])
    
    def cal(self, v2, v1, sig):
        if sig == '+':
            return str(v2 + v1)
        if sig == '-':
            return str(v2 - v1)
        if sig == '*':
            return str(v2 * v1)
        if sig == '/':
            return str(int(v2 / v1))
