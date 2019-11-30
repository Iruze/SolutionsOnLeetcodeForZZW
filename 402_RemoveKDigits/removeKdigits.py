class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or k > len(num) or k < 0:
            return '0'
        stack = []
        n, m = len(num), len(num) - k
        for e in num:
            while k > 0 and stack and stack[-1] > e:
                stack.pop()
                k -= 1
            stack.append(e)
        res = ''.join(stack[:m])
        while res and res[0] == '0':
            res = res[1:]
        return res if res else '0'
