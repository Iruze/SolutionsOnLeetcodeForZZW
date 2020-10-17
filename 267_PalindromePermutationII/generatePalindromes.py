class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        # 1. 判断是是否可以重新排列为回文串
        count = collections.Counter(s)
        if len([*filter(lambda x: x & 1, count.values())]) > 1:
            return []
        # 2. 将s的字符减半
        s, odd = '', ''
        for char, cnt in count.items():
            # 回文串中心可能含单个字符，做特殊处理
            if cnt & 1:
                odd = char
            s += char * (cnt // 2)
        s = sorted(list(s))
        # 3. 调用全排列II算法
        ans = []
        self._backtrack(s, odd, ans)
        return list(set(ans))
    
    # 回溯算法-全排列II
    def _backtrack(self, s, odd, ans, depth=0, visited=0, cur=[]):
        if depth == len(s):
            half = ''.join(cur)
            ans.append(half + odd + half[::-1])
            return 
        for i, c in enumerate(s):
            if visited & (1<<i) == 0:
                if i > 0 and s[i] == s[i - 1] and visited & (1 << (i - 1)) == 0:
                    continue
                self._backtrack(s, odd, ans, depth + 1, visited | (1<<i), cur + [s[i]])
