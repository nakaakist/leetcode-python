from random import choice


class RandomizedSet:
    def __init__(self):
        self.keys = []
        self.data = {}

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        else:
            self.data[val] = len(self.keys)
            self.keys.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.data:
            i_del = self.data[val]
            v_swap = self.keys[len(self.keys) - 1]
            self.keys[i_del] = v_swap
            self.data[v_swap] = i_del
            del self.data[val]
            self.keys.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.keys)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
