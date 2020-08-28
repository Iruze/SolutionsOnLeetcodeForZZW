# 定义
[参考- Trie 吐血攻略，包教包会](https://leetcode-cn.com/problems/short-encoding-of-words/solution/99-java-trie-tu-xie-gong-lue-bao-jiao-bao-hui-by-s/)
> 字典树又名前缀树，Trie树，是一种存储大量字符串的树形数据结构，相比于HashMap存储，在存储单词（和语种无关，任意语言都可以）的场景上，节省了大量的内存空间。      
下图演示了一个保存了8个单词的字典树的结构，8个单词分别是：`A`, `to`, `tea`, `ted, `ten, `i, `in, `inn`。


![字典树1](./相关的图/字典树1.png)

从根节点走到叶子节点，尝试走一下所有的路径.
**每条从根节点到叶子节点的路径都构成了单词
（有的不需要走到叶子节点也是单词，比如 `i` 和 `in`）**。
trie树里的每个节点只需要保存当前的字符就可以了
（当然你也可以额外记录别的信息，比如记录一下如果以当前节点结束是否构成单词）。

从根节点出发的路径，都是给定单词列表里某个/某些单词的前缀。
反之，如果某个字符串没有出现在这棵树的路径上，那就肯定不是某个单词的前缀。
上面说很明显这题是用字典树来做，原因就是：**这类很明显是用字典树去做的题目，
明显特征就是需要大量地判断某个字符串是否是给定单词列表中的前缀/后缀。** 
为什么要说后缀也可以呢？因为把单词倒着插入，就可以搜后缀了~

trie节点的定义(trie的根节点定义为一个空节点):
```python
class TrieNode:
    
    def __init__(self):
        self.children = dict()
```

插入单词的操作:
```python
def insert(word):
    cur = root
    for w in word:
        if w not in cur:
            cur[w] = TrieNode()
        cur = cur[w]
```

- [820. 单词的压缩编码](https://leetcode-cn.com/problems/short-encoding-of-words/)
> 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。   
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。      
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。      
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？      

示例：
```
输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
```
<details>
    <summary>字典树-list版</summary>
    
```python3
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        # 1. 先插入长的单词,比如time,这样碰到me就不用在插入了
        # 2. 根据题意, 需要是后缀搜索,故需要单词反着插入
        #    比如time, me则后缀都是me,反着插入即是em前缀
        return sum(trie.insert(word) for word in sorted(words, key=len, reverse=True))
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        is_new = False
        cur = self.root
        for i in range(len(word) - 1, -1, -1):
            idx = ord(word[i]) - ord('a')
            if cur.children[idx] is None:
                is_new = True
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        return len(word) + 1 if is_new else 0


class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
```
</details>

<details>
    <summary>字典树-dict版</summary>
    
```python3
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        #words = list(set(words))
        return sum(trie.insert(word) for word in sorted(words, key=len, reverse=True))


class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        is_new = False
        cur = self.root
        for w in word[::-1]:
            if w not in cur.children:
                is_new = True
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        return len(word) + 1 if is_new else 0


class TrieNode:
    
    def __init__(self, val=None):
        self.children = dict()
```
</details>

<details>
    <summary>字典树-pythonic版</summary>
    
[参考- 单词的压缩编码](https://leetcode-cn.com/problems/short-encoding-of-words/solution/dan-ci-de-ya-suo-bian-ma-by-leetcode-solution/314321)
```python3
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

```
</details>

- [208. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)
> 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:
```shell script
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
```
![](./相关的图/字典树2.png)
<details>
    <summary>解题思路</summary>
    
```python3
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
        trie = self.lookup
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
        """
        必须以标志字符结尾,不能靠{}为空来判断
        因为,存在重叠情况apple, app, app的结尾不为空,但是app可能存在也可能不存在
        """
        trie['$'] = '$'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.lookup
        for w in word:
            if w not in trie:
                return False
            trie = trie[w]
        return '$' in trie


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.lookup
        for w in prefix:
            if w not in trie:
                return False
            trie = trie[w]
        return True
```
</details>

##### 其他字典树题目:
- [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/)
- [126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)
- [79. 单词搜索](https://leetcode-cn.com/problems/word-search/)
- [212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)
- [面试题 17.22. 单词转换](https://leetcode-cn.com/problems/word-transformer-lcci/)
- [面试题 17.13. 恢复空格](https://leetcode-cn.com/problems/re-space-lcci/)
- [leetcode-trie集合](https://leetcode-cn.com/tag/trie/)