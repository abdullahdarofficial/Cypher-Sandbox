class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # if not nums1 or not nums2 or k <= 0:
        #     return []
        
        # mina = 0
        # minb = 0

        # lis = [[nums1[mina], nums2[minb]]]
        # i = j = 1
        # while i < len(nums1) and j < len(nums2) and mina < len(nums1) and minb < len(nums2) and k > len(lis):
        #     print(lis)
        #     option1 = nums1[mina] + nums2[j]
        #     option2 = nums2[minb] + nums1[i]
        #     option3 = nums1[mina + 1] + nums2[minb + 1]

        #     if option1 == min(option1, option2, option3):
        #         lis.append([nums1[mina] , nums2[j]])
        #         j += 1
        #     elif option2 == min(option1, option2, option3):
        #         lis.append([nums1[i], nums2[minb]])
        #         i += 1
        #     else:
        #         lis.append([nums1[mina + 1] + nums2[minb + 1]])
        #         mina += 1
        #         minb += 1
        #         i = mina + 1
        #         j = minb + 1
        #     if i == len(nums1) or j == len(nums2):
        #         mina += 1
        #         minb += 1
        #         i = mina + 1
        #         j = minb + 1
                
        
        # return lis

        if not nums1 or not nums2 or k <= 0:
            return []

        minHeap = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

        result = []

        while minHeap and len(result) < k:
            curr_sum, i, j = heapq.heappop(minHeap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i , j + 1))

        return result