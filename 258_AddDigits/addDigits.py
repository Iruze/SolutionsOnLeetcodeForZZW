class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        return self.addDigits(sum(map(int, list(str(num)))))
