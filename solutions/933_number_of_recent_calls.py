from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)


obj = RecentCounter()
p1 = obj.ping(1)
p2 = obj.ping(100)
p3 = obj.ping(3001)
p4 = obj.ping(3002)
print(p1, p2, p3, p4)
