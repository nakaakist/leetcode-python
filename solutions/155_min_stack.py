class MinStack:
    def __init__(self):
        self.mins = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mins[-1]:
            self.mins.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
