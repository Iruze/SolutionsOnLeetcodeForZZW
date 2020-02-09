class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if len(cont) == 1:
            return[cont[0], 1]
        res = [cont[-1], 1]
        for i in range(len(cont) - 2, -1, -1):
            res[0], res[1] = res[1], res[0]
            res[0] += cont[i] * res[1]
            gcd = math.gcd(res[0], res[1])
            res = list(map(lambda x: x // gcd, res))
        return res
