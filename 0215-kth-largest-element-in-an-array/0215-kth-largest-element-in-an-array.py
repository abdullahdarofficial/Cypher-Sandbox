class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # if not nums or k > len(nums):
        #     return nums
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, -num)

        # for i in range(k - 1):
        #     heapq.heappop(heap)
        # return -heapq.heappop(heap)

        if not nums or k > len(nums):
            return nums

        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k - 1):
            heapq.heappop(heap)
        return - heapq.heappop(heap)