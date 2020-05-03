class Solution:
    def maxPoints(self, points):
        points_dict = Counter(tuple(p) for p in points)
        points_set = list(points_dict.keys())
        n = len(points_set)
        if n == 1:
            return points_dict[points_set[0]]
        ans = 0
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)
        
        for i in range(n - 1):
            slope = collections.defaultdict(int)
            x1, y1 = points_set[i]
            for j in range(i + 1, n):
                x2, y2 = points_set[j]
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dy, dx)
                if g != 0:
                    dx, dy = dx // g, dy // g 
                # 统计当前点(x, y)下的斜率
                slope["{}/{}".format(dy, dx)] += points_dict[points_set[j]]
            ans = max(ans, max(slope.values()) + points_dict[points_set[i]])
        return ans
