# 方法一： 哈希 + 两两逐个比较
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def comp(word1, word2):
            if not word1: return True
            if not word2: return not word1
            if word1[0] == word2[0]:
                return comp(word1[1:], word2[1:])
            return d[word1[0]] < d[word2[0]]
        
        if len(words) < 2: return True
        d = dict()
        for l in order:
            d[l] = order.index(l)
        for i in range(len(words) - 1):
            if not comp(words[i], words[i + 1]):
                return False
        return True
        
# 方法二: 利用python排序算法sorted里面的key
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: [*map(order.index, w)])
