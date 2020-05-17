import collections
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = list()
        self.pos = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.lst.append(val)
        self.pos[val].add(len(self.lst) - 1)
        return len(self.pos[val]) == 1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.pos[val]: return False
        removal, last = self.pos[val].pop(), self.lst[-1]
        self.lst[removal] = last
        # 这两句调换可能就执行出错，
        # 先add， 后remove，就能保证不会出错
        self.pos[last].add(removal)
        self.pos[last].remove(len(self.lst) - 1)

        self.lst.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
