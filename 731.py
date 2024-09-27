class MyCalendarTwo:

    def __init__(self):
        self.single = []
        self.double = []
    def book(self, start: int, end: int) -> bool:

        for interval in self.double:
            if max(interval[0],start) < min(interval[1],end):
                return False
        for interval in self.single:
            if max(interval[0],start) < min(interval[1],end):
                self.double.append((max(interval[0],start), min(interval[1],end)))
        self.single.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)