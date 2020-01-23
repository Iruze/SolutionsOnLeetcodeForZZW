class Solution:
    def myAtoi(self, str1: str) -> int:
        str1 = str1.strip()
        if not str1: return 0
        if str1[0] == '-' or str1[0] == '+':
            pn = str1[0]
            str1 = str1[1:]
            if not str1: return 0
        else:
            pn = ''
        str_set = [str(i) for i in range(0, 10)]
        if str1[0] not in str_set: return 0
        res = ''
        for s in str1:
            if s in str_set:
                res += s
            else:
                break
        res = int(res)
        if pn == '-':
            if res >= 2147483648:
                res = 2147483648
            res = - res
        elif res >= 2147483648:
            res = 2147483647
        return res
