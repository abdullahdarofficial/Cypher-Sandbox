class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # result = {}
        # for num in arr:
        #     diff = abs(num - x)
        #     if diff not in result:
        #         result[diff] = num
        #     else:
        #         result[diff] = min(result[diff], num)

        # if not arr:
        #     return []
        
        # heap = []
        # n = len(arr)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if abs(arr[i] - x) < abs(arr[j] - x):
        #             # check i
        #             num = arr[i]
        #             diff = abs(arr[i]-x)
        #         elif abs(arr[i] - x) > abs(arr[j] - x):
        #             # check j
        #             num = arr[j]
        #             diff = abs(arr[j]-x)
        #         else:
        #             diff = abs(arr[i] - x)
        #             # check smaller of both
        #             num = min(arr[i], arr[j])
                
        #         if len(heap) < k:
        #             heapq.heappush(heap, (-num, diff))
        #         else:
        #             if not heap:
        #                 continue
        #             -prev_num, prev_diff = heap[0]
        #             if prev_diff > diff:
        #                 heapq.heappop(heap)
        #                 heapq.heappush(heap, (-num, diff))
        #             elif prev_diff == diff:
        #                 if prev_num > num:
        #                     heapq.heappop(heap)
        #                     heapq.heappush(heap, (-num, diff))
        # result = []
        # while heap:
        #     result.append(-heapq.heappop(heap)) 
        # return result



        if not arr:
            return []

        heap = []

        for num in arr:
            diff = abs(num - x)
            heapq.heappush(heap, (diff, num))

        result = []
        for _ in range(k):
            if heap:
                result.append(heapq.heappop(heap)[1])

        return sorted(result)            




        