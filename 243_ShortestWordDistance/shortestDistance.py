class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        l1 = l2 = -1
        res = len(words)
        for idx, word in enumerate(words):
            if word == word1:
                l1 = idx
            if word == word2:
                l2 = idx
            if l1 != -1 and l2 != -1:
                res = min(res, abs(l1 - l2))
        return res
