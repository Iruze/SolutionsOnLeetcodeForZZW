class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        l1, l2 = len(v1), len(v2)
        i1, i2 = 0, 0
        while i1 < l1 or i2 < l2:
            c1 = int(v1[i1]) if i1 < l1 else 0
            c2 = int(v2[i2]) if i2 < l2 else 0
            if c1 > c2:
                return 1
            elif c1 < c2:
                return -1
            i1, i2 = i1 + 1, i2 + 1
        return 0
