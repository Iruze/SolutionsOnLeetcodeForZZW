class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        # 字符串以'$'结尾
        tree['$'] = '$'


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        return '$' in tree


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
