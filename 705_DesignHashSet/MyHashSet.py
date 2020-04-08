class Bucket:

    def __init__(self):
        self.buckt = []


    def add(self, key):
        if key not in self.buckt:
            self.buckt.append(key)
    

    def remove(self, key):
        for i, k in enumerate(self.buckt):
            if k == key:
                del self.buckt[i]
    

    def contains(self, key):
        return key in self.buckt

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]
        

    def add(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].add(key)
        

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].contains(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
