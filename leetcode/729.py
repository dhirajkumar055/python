from collections import defaultdict
class MyCalendar:

    def __init__(self):
        self.d=defaultdict(list)

    def book(self, start: int, end: int) -> bool:
        for i in self.d:
            if start>=i[0] and start<i[1] or end>i[0] and end<=i[1] or start<=i[0] and end>i[1]:
                return False
        
        self.d[tuple([start,end])]=[start,end]
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
l=[[19,30],[18,37],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
for start,end in l:
    obj.book(start,end)


# ["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
# [[],[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]