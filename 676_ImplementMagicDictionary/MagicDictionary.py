#方法一： 常规哈希
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = collections.defaultdict(set)


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                self.lookup[word[:i] + '*' + word[i+1:]].add(word)


    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            sea = searchWord[:i] + '*' + searchWord[i+1:]
            if self.lookup[sea] and (searchWord not in self.lookup[sea] or len(self.lookup[sea]) > 1):
                return True
        return False

# 方法二： 字典树 + DFS
class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        # 一个完整单词的结束标志
        self.isword = False


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for c in word:
                node = node.children[c]
            # 当前node是字典中一个完整单词的结尾
            node.isword = True


    def search(self, searchWord: str) -> bool:
        def searchCore(node, word, changed_once=False):
            for i, c in enumerate(word):
                if changed_once:
                    # 如果已经变换过一次，现在又找不到匹配的
                    if c not in node.children:
                        return False
                    # 如果已经变换过一次，但是找到匹配的，则沿着匹配的c继续
                    node = node.children[c]
                elif c not in node.children:
                    # c不存在于当前的children中，则给一次变换的机会，
                    for nxt in node.children:
                        # 搜索所有的children向下搜索
                        if searchCore(node.children[nxt], word[i+1:], True):
                            return True
                    # 给一次变换的机会，仍然搜索不到匹配的
                    return False
                else:
                    # c匹配当前的node，但是尝试将c匹配到不等于c的node的children中去，并记一次changed_once
                    for nxt in node.children:
                        # 如果给一次changed机会，且匹配上了
                        if nxt != c and searchCore(node.children[nxt], word[i+1:], True):
                            return True
                    # 上面的搜索没有结果，但是不影响c匹配当前node的情况时继续向下搜索
                    node = node.children[c]
            # 如果当前的node是字典中单词的结尾，且有了一次changed的，则认为匹配到了结果
            return node.isword and changed_once
        return searchCore(self.root, searchWord)
