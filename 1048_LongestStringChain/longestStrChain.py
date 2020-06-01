"""
１．words按照字符串长短排序；

２. 扫描words, 挨个尝试其前身，如果存在，则以当前word结尾的字符串链自增1
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # words按照字符串长短排序
        words.sort(key=len)
        maxChain, count = 1, dict()
        for word in words:
            if word not in count:
                count[word] = 1
            # 依次去掉word中的一个字符，挨个尝试word的前身
            for i, c in enumerate(word):
                pre = word[:i] + word[i + 1:]
                # 若前身存在，　则以word结尾的字符串链长度自增１
                if pre in count:
                    count[word] = max(count[word], count[pre] + 1)
            maxChain = max(maxChain, count[word])
        return maxChain
