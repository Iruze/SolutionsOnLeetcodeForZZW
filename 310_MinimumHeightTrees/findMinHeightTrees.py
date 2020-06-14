"""
python3, bfs
参考：https://leetcode-cn.com/problems/minimum-height-trees/solution/tan-xin-fa-gen-ju-tuo-bu-pai-xu-de-si-lu-python-da/
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 画图，刻画所有节点的连接关系
        graph = collections.defaultdict(list)
        # 求每个节点的“度”，即和周围连接的节点个数
        degree = [0] * n
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            degree[x] += 1
            degree[y] += 1
        # 叶子节点，bfs从最外层的叶子节点开始一层一层地“消减”
        leaves = [i for i in range(n) if len(graph[i]) == 1] if n > 1 else [0]
        leaves_nxt = []
        rst = n
        # 当且仅当“消减”到只有1或2个节点的时候，则是剩下的节点是“最小高度树”的根
        while rst > 2:
            # 减掉当前层的所有叶子节点的数目
            rst -= len(leaves)
            for i in leaves:
                degree[i] = 0
                for con in graph[i]:
                    if degree[con] > 0:
                        # 因为con连接的叶子节点已经被“消减”，故con的“度”也应该减少1
                        degree[con] -= 1
                        if degree[con] == 1:
                            leaves_nxt.append(con)
            leaves, leaves_nxt = leaves_nxt, leaves
            leaves_nxt = []
        return leaves
