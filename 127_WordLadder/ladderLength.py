class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        深度优先搜索
        """
        wordList_dict = collections.defaultdict(list)
        for word in wordList:
            for i, c in enumerate(word):
                wordList_dict[word[:i] + '*' + word[i+1:]].append(word)
        visited = {beginWord}
        # queue记录层次遍历的序列
        queue = collections.deque([(beginWord, 1)])
        while queue:
            cur, depth = queue.popleft()
            if cur == endWord:
                return depth
            for i, c in enumerate(cur):
                tmp = cur[:i] + '*' + cur[i+1:]
                # 搜索当前cur变换一个字符后的结果
                for nxt in wordList_dict[tmp]:
                    if nxt not in visited:
                        visited.add(nxt)
                        # 下一层的结果入队
                        queue.append([nxt, depth + 1])
        return 0
