class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.dict = [Node() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash(key)
        node = self.dict[hash_key]

        while node.next:
            node = node.next
            if node.key == key:
                node.value = value
                return
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        hash_key = self._hash(key)
        node = self.dict[hash_key].next

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        node = self.dict[hash_key]

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
