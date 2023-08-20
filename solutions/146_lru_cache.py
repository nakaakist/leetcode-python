class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def _remove(self, key):
        if key not in self.pointers:
            return -1

        node = self.pointers[key]
        del self.pointers[key]

        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        else:
            self.queue_head = next
        if next:
            next.prev = prev
        else:
            self.queue_tail = prev

        return node.val

    def _append(self, key, val):
        node = ListNode(key, val, self.queue_tail, None)
        self.pointers[key] = node

        if self.queue_tail:
            self.queue_tail.next = node
        if not self.queue_head:
            self.queue_head = node
        self.queue_tail = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue_head = None
        self.queue_tail = None
        self.pointers = {}

    def get(self, key: int) -> int:
        val = self._remove(key)
        if val == -1:
            return val
        else:
            self._append(key, val)
            return val

    def put(self, key: int, value: int) -> None:
        self._remove(key)
        self._append(key, value)

        if len(self.pointers) > self.capacity:
            self._remove(self.queue_head.key)


# # Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(2)
print(lRUCache.put(1, 1))
print(lRUCache.put(2, 2))
print(lRUCache.get(1))
print(lRUCache.put(3, 3))
print(lRUCache.get(2))
print(lRUCache.put(4, 4))
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))

lRUCache = LRUCache(1)
print(lRUCache.put(2, 1))
print(lRUCache.get(2))
