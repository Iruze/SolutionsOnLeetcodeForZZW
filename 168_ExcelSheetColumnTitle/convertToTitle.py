class Solution:
    def convertToTitle(self, n: int) -> str:
        # 映射表 0-25 映射字母 ‘A’ - ‘Z’
        table = [*map(chr, range(65, 91))]
        # 递归解法
        if n <= 26: return table[n - 1]
        return self.convertToTitle((n - 1) // 26) + table[(n - 1) % 26]
