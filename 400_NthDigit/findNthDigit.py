class Solution:
    def findNthDigit(self, n: int) -> int:
        # n - 1的目的在于，后面first_num的第一个索引从0开始
        n -= 1
        # pow(2, 31) < pow(10, 11), 在32位证书范围内
        for digit in range(1, 11):
            # [first_num]表示每一组第一个数
            # [1]23456789       [10]11...99     [100]101...999
            first_num = 10 ** (digit - 1)
            if n < 9 * first_num * digit:
                return int(str(first_num + n / digit)[n % digit])
            n -= 9 * first_num * digit
        return -1
