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
## 无向图
- [886. 可能的二分法](https://leetcode-cn.com/problems/possible-bipartition/)
>给定一组 `N` 人（编号为 `1`, `2`, ..., `N`）， 我们想把每个人分进任意大小的两组。    
每个人都可能不喜欢其他人，那么他们不应该属于同一组。    
形式上，如果 `dislikes[i] = [a, b]`，表示不允许将编号为 `a` 和 `b` 的人归入同一组。    
当可以用这种方法将每个人分进两组时，返回 `true`；否则返回`false`。

>示例 1：    
输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]   
输出：true    
解释：group1 [1,4], group2 [2,3]    

>示例 2：    
输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]     
输出：false   

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