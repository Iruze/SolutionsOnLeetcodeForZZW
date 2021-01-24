# 解法一: x的权重为x_w, 对 (x_w, x)进行排序
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        rank = dict()
        for i in range(lo, hi + 1):
            rank[i] = self.steps(i)
        rank = sorted([*zip(rank.keys(), rank.values())], key=lambda x:(x[1], x[0]))
        return rank[k - 1][0]
    
    def steps(self, num):
        if num == 1: return 0
        if num & 1 == 1:
            return 1 + self.steps(3 * num + 1)
        return 1 + self.steps(num // 2)


# 解法二: 自定义排序, 直接对x进行排序
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        @functools.lru_cache(None)                      # 缓存x的权重值,对于重复的x相当于查询其权重值
        def cal_weigth(x):
            if x == 1:
                return 0
            elif x & 1:
                return 1 + cal_weigth(3 * x + 1)
            else:
                return 1 + cal_weigth(x // 2)
        
        def my_cpm(x, y):                               # 自定义排序
            x_w, y_w = cal_weigth(x), cal_weigth(y)
            if x_w == y_w:                              # 权重相同, 按照自身值大小排序
                return x - y
            return x_w - y_w

        nums = [*range(lo, hi + 1)]
        nums.sort(key=functools.cmp_to_key(my_cpm))
        return nums[k - 1]            
