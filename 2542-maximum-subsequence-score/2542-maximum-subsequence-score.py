class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # heap1 = []
        # for index, num in enumerate(nums1):
        #     heapq.heappush(heap1, (-num, index))

        # heap2 = []
        # for index, num in enumerate(nums2):
        #     heapq.heappush(heap2, (-num, index))


        # numsum = 0
        # nummin = float("inf")
        # for _ in range(k):
        #     if heap1 and (not heap2 or heap1[0][0] >= heap2[0][0]):
        #         num, index = heapq.heappop(heap1)
        #         numsum += -num
        #         nummin = min(nummin, nums2[index])
        #     else:
        #         num, index = heapq.heappop(heap2)
        #         numsum += nums1[index]
        #         nummin = min(nummin, nums2[index])


        
        # return numsum * nummin


        pairs = sorted(zip(nums1, nums2), key = lambda x : x[1], reverse = True)
        max_score = 0
        current_sum = 0
        min_heap = []

        for i in range(len(pairs)):
            heapq.heappush(min_heap, pairs[i][0])
            current_sum += pairs[i][0]

            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, current_sum * pairs[i][1])

        return max_score



        
