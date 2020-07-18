解题步骤：
- 画无向图graph
- dict设置预分组/记录轨迹
- 遍历不在dict中的节点，根据graph图，dfs查找当前节点的相邻节点

- [886. 可能的二分法](https://leetcode-cn.com/problems/possible-bipartition/)
```shell
给定一组 `N` 人（编号为 `1`, `2`, ..., `N`）， 我们想把每个人分进任意大小的两组。

每个人都可能不喜欢其他人，那么他们不应该属于同一组。

形式上，如果 `dislikes[i] = [a, b]`，表示不允许将编号为 `a` 和 `b` 的人归入同一组。

当可以用这种方法将每个人分进两组时，返回 `true`；否则返回`false`。
```
```shell
示例 1：

输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]


示例 2：

输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
```

解题：
```python3
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # 将dislike画成联通的无向图
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = dict()
        def dfs(i, c = 1):
            if i in color:
                return c == color[i]
            # 节点i未染色，和i相邻的节点也未染色，故默认染色为1
            color[i] = c
            # 将节点i的所有相邻节点染色为-1，都不存在染色冲突则返回True
            return all(dfs(j, -1 * c) for j in graph[i])
        
        return all(dfs(i) for i in range(1, N + 1) if i not in color)
```

- [785. 判断二分图](https://leetcode-cn.com/problems/is-graph-bipartite/)
```shell
给定一个无向图`graph`，当这个图为二分图时返回`true`。

如果我们能将一个图的节点集合分割成两个独立的子集`A`和`B`，并使图中的每一条边的两个节点一个来自`A`集合，一个来自`B`集合，我们就将这个图称为二分图。

`graph`将会以邻接表方式给出，`graph[i]`表示图中与节点`i`相连的所有节点。每个节点都是一个在`0`到`graph.length-1`之间的整数。这图中没有自环和平行边： `graph[i]` 中不存在`i`，并且`graph[i]`中没有重复的值。
```

解题：
```python3
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        group = dict()
        # dfs判断是否可以将节点i放在组g中去，默认放在组1
        def dfs(i, g = 1):
            if i in group:
                return group[i] == g 
            group[i] = g
            # 将节点i相邻的所有节点放在组-1中，如果不存在任何冲突，则返回True
            return all(dfs(j, -1 * g) for j in graph[i])
        
        return all(dfs(i) for i in range(len(graph)) if i not in group)
```
