class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.n = 1000
        self.container = [None] * self.n

    def _hash(self, key: int):
        return key % self.n

    def _find(self, key: int, hash_key: int):
        ...

    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        val = self.container[hash_key]
        if val == None:
            self.container[hash_key] = []
        i = 0
        found = False
        for num in self.container[hash_key]:
            if num == key:
                found = True
                break
        if found:
            return
        self.container[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        if self.container[hash_key] is not None:
            i = 0
            while i < len(self.container[hash_key]):
                if self.container[hash_key][i] == key:
                    del self.container[hash_key][i]
                    return
                i += 1

    def contains(self, key: int) -> bool:
        hash_key = self._hash(key)
        if self.container[hash_key] is not None:
            for val in self.container[hash_key]:
                if val == key:
                    return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
