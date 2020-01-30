class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = ''
        carry = 0
        while i >= 0 or j >= 0:
            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            i, j = i - 1, j - 1
        return res if not carry else '1' + res
