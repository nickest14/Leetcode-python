# 729. My Calendar I


class MyCalendar:

    def __init__(self):
        self.bookings: list[tuple[int]] = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if start < e and end > s:
                return False
        self.bookings.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))
