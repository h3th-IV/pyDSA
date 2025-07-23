class Node:
    def __init__(self, key=0, value=''):
        self.prev = None
        self.key = key
        self.value = value
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # dummy head and tail for simplicity
        self.head = Node()  # Most recently used
        self.tail = Node()  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

    def print(self):
        print(self.cache)
            

cache = LRUCache(4)  # Capacity = 2
cache.put(1, 'Yarn Miller')  # cache is {1=1}
cache.put(2, 'Wool Miller')  # cache is {1=1, 2=2}
cache.put(4, 'Thread Miller')  # cache is {1=1, 2=2}
cache.put(5, 'Cotton Miller')  # cache is {1=1, 2=2}
print(cache.get(1))  # returns 1
cache.put(3, 'Poly Miller')  # evicts key 2, cache is {1=1, 3=3}
print(cache.get(2))
cache.print()