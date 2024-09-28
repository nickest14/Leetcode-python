# 731. My Calendar II


class MyCalendarTwo:

    def __init__(self):
        self.calendar: list[tuple[int, int]] = []
        self.overlaps: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        for date in self.overlaps:
            if start < date[1] and end > date[0]:
                return False

        for date in self.calendar:
            if start < date[1] and end > date[0]:
                self.overlaps.append((max(date[0], start), min(date[1], end)))
        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendarTwo()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.book(25, 55))
