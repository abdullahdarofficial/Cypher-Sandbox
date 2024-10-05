class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        for i in range(1, 10000):
            heapq.heappush(self.heap, i)

    def popSmallest(self) -> int:
        if not self.heap:
            return 0
        return heapq.heappop(self.heap)
         
        

    def addBack(self, num: int) -> None:
        if num in self.heap:
            return
        heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)