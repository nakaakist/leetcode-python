class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        days = 1
        while self.stack and self.stack[-1][1] <= price:
            cont_days, _ = self.stack.pop()
            days += cont_days
        self.stack.append((days, price))

        return days


stockSpanner = StockSpanner()
print(stockSpanner.next(100))
print(stockSpanner.next(80))
print(stockSpanner.next(60))
print(stockSpanner.next(70))
print(stockSpanner.next(60))
print(stockSpanner.next(75))
print(stockSpanner.next(85))
