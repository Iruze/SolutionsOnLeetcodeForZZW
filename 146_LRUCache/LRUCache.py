# 参考
# https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/


class LinkNode:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.pos = dict()
        self.capacity = capacity
    
    def move_to_end(self, key):
        node = self.pos[key]
        node.pre.nxt, node.nxt.pre = node.nxt, node.pre
        self.tail.pre.nxt, node.pre = node, self.tail.pre
        node.nxt, self.tail.pre = self.tail, node

    def get(self, key: int) -> int:
        if key not in self.pos:
            return -1
        self.move_to_end(key)
        return self.pos[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.pos:
            self.move_to_end(key)
            self.pos[key].value = value
        else:
            if len(self.pos) == self.capacity:
                del self.pos[self.head.nxt.key]
                v_head = self.head.nxt.nxt
                self.head.nxt, v_head.pre = v_head, self.head
            new_node = LinkNode(key, value)
            self.pos[key] = new_node
            self.tail.pre.nxt, new_node.pre = new_node, self.tail.pre
            new_node.nxt, self.tail.pre = self.tail, new_node


