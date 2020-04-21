class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        candidate = list(count.keys())
        candidate.sort(key=lambda x:(-count[x], x))
        return candidate[:k]
