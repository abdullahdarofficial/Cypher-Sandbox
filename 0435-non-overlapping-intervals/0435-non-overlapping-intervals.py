class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return None

        intervals.sort(key=lambda x: x[1])
        i = 1
        count = 0
        end = intervals[0][1]
        while i < len(intervals):
            if end > intervals[i][0]:
                count += 1
            else:
                end = intervals[i][1]      
            i += 1      
        return count


