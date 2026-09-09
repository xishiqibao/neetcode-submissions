class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(Node)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        temp1 = node.prev
        temp2 = node.next
        temp1.next = temp2
        temp2.prev = temp1

    def insert(self, node):
        temp1 = self.right.prev
        temp2 = self.right
        temp1.next = temp2.prev = node
        node.next = temp2
        node.prev = temp1

    def get(self, key: int) -> int:
        if(key in self.cache):
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        
        if(len(self.cache) > self.capacity):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
