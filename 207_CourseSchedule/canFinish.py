class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for cur, pre in prerequisites:
            graph[cur].append(pre)
        course = set()

        @functools.lru_cache(None)      # 缓存中间结果,下次相同的cur就相当于表查询,直接返回
        def dfs(cur):
            if cur in course:           # cur在course中, 证明存在环
                return False
            course.add(cur)
            for pre in graph[cur]:      # 递归检测是否存在环
                if not dfs(pre):
                    return False
            course.remove(cur)          # 回溯思想: 当cur开始的路径不存在环, 退出cur
            return True
        
        for num in range(numCourses):   # 检测所有的课程
            if not dfs(num):
                return False
        return True
        
