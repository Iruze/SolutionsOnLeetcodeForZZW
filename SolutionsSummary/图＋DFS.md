# 解题步骤：
**1). 画图graph**
```python
graph = collections.defaultdict(list)

# 有向图
for cur, pre in prerequisites:
    graph[cur].append(pre)

# 无向图
for i, j in prerequisites:
    graph[cur].append(pre)
    graph[pre].append(cur)
```

**2). 记录visted**  
`dict`设置预分组/记录轨迹        
或者, `pre_set`记录当前已经访问的**节点**

**3). DFS下一层遍历**     
不在dict中的节点，根据graph图，dfs查找当前节点的相邻节点


# 例题
## 无向图(连通图)
给定的无向图一般默认是**连通图**
- [886. 可能的二分法](https://leetcode-cn.com/problems/possible-bipartition/)
>给定一组 `N` 人（编号为 `1`, `2`, ..., `N`）， 我们想把每个人分进任意大小的两组。    
每个人都可能不喜欢其他人，那么他们不应该属于同一组。    
形式上，如果 `dislikes[i] = [a, b]`，表示不允许将编号为 `a` 和 `b` 的人归入同一组。    
当可以用这种方法将每个人分进两组时，返回 `true`；否则返回`false`。

>示例 1：    
输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]   
输出：true    
解释：group1 [1,4], group2 [2,3]       

<details>
    <summary>解法</summary>
    
```python
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

</details>


- [785. 判断二分图](https://leetcode-cn.com/problems/is-graph-bipartite/)

>给定一个无向图`graph`，当这个图为二分图时返回`true`。      
如果我们能将一个图的节点集合分割成两个独立的子集`A`和`B`，并使图中的每一条边的两个节点一个来自`A`集合，一个来自`B`集合，我们就将这个图称为二分图。         
`graph`将会以邻接表方式给出，`graph[i]`表示图中与节点`i`相连的所有节点。每个节点都是一个在`0`到`graph.length-1`之间的整数。这图中没有自环和平行边： `graph[i]` 中不存在`i`，并且`graph[i]`中没有重复的值。


<details>
    <summary>解法</summary>
    
```python
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
</details>

- [399. 除法求值](https://leetcode-cn.com/problems/evaluate-division/)
> 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。       
另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。        
返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。     
注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。     
```shell script
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
```

本题两种解法- **并查集**和**无向图DFS**
<details>
    <summary>解法一 图DFS</summary>
    
```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        var = set()
        # 注意set中update的用法
        for item, value in zip(equations, values):
            var.update(item)
            s, e = item[0], item[1]
            # 刻画无向图
            graph[s][e] = value
            graph[e][s] = 1.0 / value

        @functools.lru_cache(None)
        def dfs(s, e):
            if s == e:
                return 1.0
            visited.add(s)
            ret = 1.0
            for nxt in graph[s]:
                if nxt not in visited:
                    ret = graph[s][nxt] * dfs(nxt, e)
                    if ret > 0:
                        return ret
            visited.remove(s)
            return -1.0
        
        ans = list()
        visited = set()
        for s, e in queries:
            if s not in var or e not in var:
                ans.append(-1.0)
            else:
                # 每次查询s-e对,负责记录的visited都是"空初始化"
                visited.clear()
                ans.append(dfs(s, e))
        return ans
```
</details>

**BFS搜索图**
- [310. 最小高度树](https://leetcode-cn.com/problems/minimum-height-trees/)
> 给你一棵包含 n 个节点的数，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。       
可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。        
请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。     


<details>
    <summary>解法一: BFS搜索 </summary>
    
```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        degree = [0] * n
        # 1. 刻画图
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
            degree[s] += 1
            degree[e] += 1
        # 2. 找到所有的"叶子节点"
        leaves = [leaf for leaf in range(n) if degree[leaf] == 1] if n > 1 else [0]
        rst = n
        # 广度优先搜索 BFS
        while rst > 2:
            # 当只有两个节点的时候, 终止搜索
            rst -= len(leaves)
            # 下一层记录
            leaves_nxt = []
            for l in leaves:
                # 当前"叶子节点"-度清零
                degree[l] = 0
                for con in graph[l]:
                    if degree[con] > 1:
                        degree[con] -= 1
                        # 找到"根节点"的标准
                        if degree[con] == 1:
                            leaves_nxt.append(con)
            # 下一层做准备
            leaves_nxt, leaves = [], leaves_nxt
        return leaves
```
</details>


## 有向图

- [207. 课程表](https://leetcode-cn.com/problems/course-schedule/)
> 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。      
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]      
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？      
```shell script
输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
```

<details>
    <summary>解法</summary>
    
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 将选修和先修课程的映射关系表示成图
        graph = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            graph[cur].append(pre)
        
        # 如果图中不存在环，即证明能够完成当前课程
        # circle记录在搜索先修课程过程中的选修课程
        circle = set()
        from functools import lru_cache
        @lru_cache(None)
        def dfs(num):
            # 如果选修课程也是先修课程，即存在了环，故不能完成当前课程
            if num in circle:
                return False
            circle.add(num)
            for pre in graph[num]:
                #　dfs思想：若先修课程不能完成，那么当前课程也算作不能完成
                if not dfs(pre):
                    return False
            circle.remove(num)
            return True

        # 挨个从当前的选修成出发，搜索其先修课程是否能够完成
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True
```
</details>