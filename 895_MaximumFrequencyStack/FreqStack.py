class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        # 不是出现的频率，而是频率的排名，值越大频率越高
        self.maxfreq = 0
        

    def push(self, x: int) -> None:
        # 1. 得到频次
        f = self.freq[x] + 1
        self.freq[x] = f
        # 2. 更新频次排名
        if f > self.maxfreq:
            self.maxfreq = f
        # 3. 入栈
        self.group[f].append(x)
        

    def pop(self) -> int:
        # 1. 得到最高频次的pop值
        x = self.group[self.maxfreq].pop()
        # 2. 更新频次
        self.freq[x] -= 1
        # 3. 更新频次排名
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
