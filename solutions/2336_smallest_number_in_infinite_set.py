from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.min_non_operated = 1
        self.operated_heap = []
        self.operated_set = set()

    def popSmallest(self) -> int:
        if len(self.operated_heap) == 0:
            ret = self.min_non_operated
            self.min_non_operated += 1
            return ret
        else:
            popped = heappop(self.operated_heap)
            self.operated_set.remove(popped)
            return popped

    def addBack(self, num: int) -> None:
        if num == self.min_non_operated - 1:
            self.min_non_operated -= 1
        elif num < self.min_non_operated - 1 and not num in self.operated_set:
            heappush(self.operated_heap, num)
            self.operated_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
print(obj.addBack(2))
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.addBack(1))
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.popSmallest())
print(obj.addBack(3))
print(obj.addBack(3))
print(obj.addBack(2))
print(obj.addBack(1))
print(obj.popSmallest())
print(obj.popSmallest())
