from heapq import heappop, heappush


class MedianFinder:
    INF = 10**10

    def __init__(self):
        self.q_low = [self.INF]
        self.mid = None
        self.q_high = [self.INF]

    def addNum(self, num: int) -> None:
        l_max, h_min = self.__low_max(), self.__high_min()
        if self.mid is not None:
            if num >= self.mid:
                self.__push_high(num)
                self.__push_low(self.mid)
            else:
                self.__push_high(self.mid)
                self.__push_low(num)
            self.mid = None
        else:
            if num < l_max:
                self.mid = self.__pop_low()
                self.__push_low(num)
            elif num < h_min:
                self.mid = num
            else:
                self.mid = self.__pop_high()
                self.__push_high(num)

    def findMedian(self) -> float:
        if self.mid is None:
            return (self.__low_max() + self.__high_min()) / 2
        else:
            return self.mid

    def __low_max(self) -> int:
        return -self.q_low[0]

    def __push_low(self, num: int):
        heappush(self.q_low, -num)

    def __pop_low(self) -> int:
        return -heappop(self.q_low)

    def __high_min(self) -> int:
        return self.q_high[0]

    def __push_high(self, num: int):
        heappush(self.q_high, num)

    def __pop_high(self) -> int:
        return heappop(self.q_high)


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
