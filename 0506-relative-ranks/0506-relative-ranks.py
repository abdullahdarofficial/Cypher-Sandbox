class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        heap = []

        for index, val in enumerate(score):
            heapq.heappush(heap, (-val, index))

        answer = [None] * len(score)
        pos = 0
        while heap:
            value, index = heapq.heappop(heap)
            if pos == 0:
                answer[index] = "Gold Medal"
            elif pos == 1:
                answer[index] = "Silver Medal"
            elif pos == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(pos + 1)
            pos += 1

        return answer

