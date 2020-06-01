"""
将字符按字符数排序。
如果最多的字符占了半数以上，返回空，
如果总字符数是偶数，将排序后的字符分为前后两半，交叉得出结果
如果为奇数，将前后两半交叉，再加上最中间的字符。
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        s = sorted(S)
        count = collections.Counter(s)
        s.sort(key=count.get)
        n = len(s) // 2
        if s[-1] == s[n - 1]:
            return ''
        a, b = s[:n], s[n:]
        for i in range(len(a)):
            s[i * 2 + 1] = a[i]
        for j in range(len(b)):
            s[j * 2] = b[j]
        return ''.join(s)
