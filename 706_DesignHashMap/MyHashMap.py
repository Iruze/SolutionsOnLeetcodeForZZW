class Bucket:

    def __init__(self):
        self.bucket = []
    

    def update(self, key, value):
        for i, item in enumerate(self.bucket):
            if item[0] == key:
                self.bucket[i] = (key, value)
                break
        else:
            self.bucket.append((key, value))
    

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
    

    def remove(self, key):
        for i, item in enumerate(self.bucket):
            if item[0] == key:
                del self.bucket[i]


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)
    

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
