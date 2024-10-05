class SmallestInfiniteSet:

    # def __init__(self):
    #     self.heap = []
    #     for i in range(1, 10000):
    #         heapq.heappush(self.heap, i)

    # def popSmallest(self) -> int:
    #     if not self.heap:s
    #         return 0
    #     return heapq.heappop(self.heap)
         
        

    # def addBack(self, num: int) -> None:
    #     if num in self.heap:
    #         return
    #     heapq.heappush(self.heap, num)
        
    def __init__(self):
        self.heap = []
        self.present = set()
        for i in range(1, 10000):
            heapq.heappush(self.heap, i)
            self.present.add(i)

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.present.remove(smallest)
            return smallest
        return 0
         
        

    def addBack(self, num: int) -> None:
        if num not in self.present:
            heapq.heappush(self.heap, num)
            self.present.add(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)