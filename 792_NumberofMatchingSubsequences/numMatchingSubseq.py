class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        head = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            head[ord(next(it)) - ord('a')].append(it)
        ans = 0
        for s in S:
            idx = ord(s) - ord('a')
            old_bucket, head[idx] = head[idx], []
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    head[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1
        return ans
