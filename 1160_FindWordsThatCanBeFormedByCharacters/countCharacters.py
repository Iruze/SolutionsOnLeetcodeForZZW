class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = dict()
        # 将字母表chars字典化
        for c in chars:
            d[c] = d.setdefault(c, 0) + 1
        ans = 0
        # 遍历词汇表words
        for w in words:
            # 遍历词汇表中的字符
            for w0 in set(w):
                if w.count(w0) > d.get(w0, -float('Inf')):
                    break
            # 注意 for-else用法
            # 如果for全部执行，则执行else，如果break跳出则不执行
            else:
                ans += len(w)
        return ans
