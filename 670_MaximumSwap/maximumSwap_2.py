class Solution:
    def maximumSwap(self, num: int) -> int:
        d = collections.defaultdict()
        num = str(num)
        for i, v in enumerate(num):
            d[v] = i
        for i, v in enumerate(num):
            for j in range(9, int(v), -1):
                if d.setdefault(str(j), -1) > i:
                    i1 = d[str(j)]
                    return int(num[:i] + num[i1] + num[i+1:i1] + num[i] + num[i1+1:])
        return int(num)
