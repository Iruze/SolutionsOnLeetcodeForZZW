class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # 解法一: 暴力解法
        # words_dict = set(words)
        # n = len(text)
        # ans = []
        # for i in range(n):
        #     for j in range(i, n):
        #         if text[i:j+1] in words_dict:
        #             ans.append([i, j])
        # return ans

        # 解法二: 字典树
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for first in range(len(text)):
            # 找到所有以first开头, 且在字典words中的字符的, 其结尾在text中的索引
            end = trie.search(text, first)
            # 将end中所有的结尾索引和first配对,放入结果中
            for e in end:
                ans.append([first, e])
        return ans


class TrieNode:

    def __init__(self):
        self.children = dict()
        # isword用来标记,以当前节点为结尾的插入是否是一个完整单词
        self.isword = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # 此时word全部插入到trie中了, cur作为结尾, isword来标志这是一个完整的word插入
        cur.isword = True

    def search(self, text, first):
        cur = self.root
        end = []
        for i in range(first, len(text)):
            # 当中间的字符不存在于trie时直接终止, 后面的绝对不会存在于trie中了
            if text[i] not in cur.children:
                break
            cur = cur.children[text[i]]
            if cur.isword:
                end.append(i)
        return end
