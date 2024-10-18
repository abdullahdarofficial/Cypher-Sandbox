class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return None

        intervals.sort(key=lambda x: x[1])
        print(intervals)
        i = 1
        count = 0
        while i < len(intervals):
            start, end = intervals[i-1]
            if end > intervals[i][0]:
                intervals.pop(i)
                count += 1
            else:
                i += 1
            
        return count


