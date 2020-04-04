class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if not text: return 0
        letter = collections.Counter(text)
        # 返回整套'balloon'字符的套数
        return min(letter['b'], letter['a'], letter['l'] // 2, letter['o'] // 2, letter['n'])
