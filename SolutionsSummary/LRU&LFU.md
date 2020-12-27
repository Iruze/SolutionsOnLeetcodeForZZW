# LRU
特点：
```shell script
1. cache缓存有容量限制
2. 最近最少访问的数据在cache达到容量上限时，会被优先删除
```

- [146. LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache/)

>实现 LRUCache 类         
LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存       
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。      
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。


解法:
```python
class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict

        self.capacity = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
```

#### collections.OrderDict的用法
```shell script
dic = collections.OrderedDict()
# copy
new_dic = dic.copy()

# clear
dic.clear()

# pop(获取指定key的value，并在字典中删除)
dic['k1'] = 'v1'
k = dic.pop('k1')
print(k,dic)    # v2 OrderedDict([('k1', 'v1'), ('k3', 'v3')])

# popitem(按照后进先出原则，删除最后加入的元素，返回key-value)
dic.popitem()                     # 移除最后一个
dic.popitem(last=False)           # 移除第一个

#move_to_end(指定一个key，把对应的key-value移到最后)
dic.move_to_end('k1')                       # 移到最后
dic.move_to_end('k1', last=False)           # 移到开头

# 其他:
跟dict都有 items(), keys(), values(), setdefault()方法, 如果dict初始化不是
顺序插入的, 即直接用一组key-value初始化, 则dict仍然是无序的.
另外, python3.6+中普通dict是有序的.
```

# LFU
