class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def __gcd(a, b):
            if b == 0: return a
            return __gcd(b, a % b)
        ab = a * b / __gcd(a, b)
        bc = b * c / __gcd(b, c)
        ac = a * c / __gcd(a, c)
        abc = a * bc / __gcd(a, bc)
        left, right = min(a, b, c), 2 * pow(10, 9)
        while left < right:
            mid = left + (right - left) // 2
            numA, numB, numC = mid // a, mid // b, mid // c
            numAB, numBC, numAC = mid // ab, mid // bc, mid // ac
            numABC = mid // abc
            num = numA + numB + numC - numAB - numBC - numAC + numABC
            if num >= n: right = mid
            else: left = mid + 1
        return left
