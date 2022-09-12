class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = ''
        carry = 0
        # 从尾到头对位相加
        while i >= 0 or j >= 0:
            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            # 二进制进位
            carry = tmp // 2
            res = str(tmp % 2) + res
            i, j = i - 1, j - 1
        # 最高位如果有进位，需要加上carry
        return res if not carry else '1' + res

    
# 解法二： 转换为数字直接相加
class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))
