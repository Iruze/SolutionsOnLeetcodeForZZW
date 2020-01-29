# 解法一： while n1 > 0 and n2 > 0:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        flag = 0
        n1, n2 = len(num1),len(num2)
        res = ''
        while n1 > 0 and n2 > 0:
            s = int(num1[n1 - 1]) + int(num2[n2 - 1]) + flag
            s, flag = s % 10, s // 10
            res = str(s) + res
            n1, n2 = n1 - 1, n2 - 1
        while n1 > 0:
            s = int(num1[n1 - 1]) + flag
            s, flag = s % 10, s // 10
            res = str(s) + res
            n1 -= 1
        while n2 > 0:
            s = int(num2[n2 - 1]) + flag
            s, flag = s % 10, s // 10
            res = str(s) + res
            n2 -= 1
        if flag:
            res = '1' + res
        return res
        
        
# 解法二： while n1 > 0 or n2 > 0:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
