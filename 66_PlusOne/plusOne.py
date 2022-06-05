class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 模拟加法进位
        carry = 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            total = digits[i] + carry + (1 if i == n - 1 else 0)
            # 十进制进位
            digits[i], carry = total % 10, total // 10
            if carry == 0:
                return digits
        return [1] + digits
