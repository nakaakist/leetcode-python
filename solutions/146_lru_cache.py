class ListNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class LRUCache:
    def _remove(self, key):
        if key not in self.pointers:
            return -1

        before, curr, after = self.pointers[key]
        before.next = after
        del self.pointers[key]
        self.pointers[before.key][2] = after
        if after is None:
            self.queue_tail = before
        else:
            self.pointers[after.key][0] = before

        return curr.val

    def _append(self, key, val):
        node = ListNode(key, val, None)
        self.queue_tail.next = node

        self.pointers[key] = [self.queue_tail, node, None]
        self.pointers[self.queue_tail.key][2] = node

        self.queue_tail = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        sentinel = ListNode(float("-inf"), None)
        self.queue_head = sentinel
        self.queue_tail = sentinel
        self.pointers = {}
        self.pointers[float("-inf")] = [None, sentinel, None]

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

        if len(self.pointers) > self.capacity + 1:
            self._remove(self.queue_head.next.key)


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
