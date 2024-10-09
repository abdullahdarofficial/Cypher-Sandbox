class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # indexes = set()
        # heap = []

        # def fillheap():
        #     i = 0 
        #     index = 0
        #     while i < (2 * candidates):
        #         if index < len(costs) and (index < candidates or index >= len(costs) - candidates):
        #             if index not in indexes:
        #                 cost = costs[index]
        #                 indexes.add(index)
        #                 heapq.heappush(heap, (cost, index))
        #             index += 1
        #         else:
        #             index = len(costs) - candidates
        #         i += 1
               
        # fillheap()
        # totalcost = 0
        # start = 0
        # end = 0
        # for i in range(k):
        #     lowCost, index = heapq.heappop(heap)
        #     totalcost += lowCost
        #     indexes.remove(index)
        #     if index < candidates + start:
        #         currindex = candidates + start
        #         if currindex not in indexes:
        #             indexes.add(currindex)
        #             heapq.heappush(heap, (costs[currindex], currindex))
        #             start += 1
        #     elif index >= len(costs) - candidates - end:
        #         currindex = len(costs) - candidates - end - 1
        #         if currindex not in indexes:
        #             indexes.add(currindex)
        #             heapq.heappush(heap, (costs[currindex], currindex))
        #             end += 1


        # return totalcost

        heap = []
        totalcost = 0
        n = len(costs)
        left , right = 0, n-1

        for i in range(candidates):
            if left <= right:
                heapq.heappush(heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(heap, (costs[right], right))
                right -= 1
        
        for _ in range(k):
            cost, idx = heappop(heap)
            totalcost += cost

            if idx < left:
                if left <= right:
                    heapq.heappush(heap, (costs[left], left))
                    left += 1
            elif idx > right:
                if left <= right:
                    heapq.heappush(heap, (costs[right], right))
                    right -= 1

        return totalcost