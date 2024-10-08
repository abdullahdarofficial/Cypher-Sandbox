class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        # isStart = False
        # out = []
        # start , end = newInterval
        # for interval in intervals:
        #     if not isStart:
        #         if start < interval[0]:
        #             interval[0] = start
        #             isStart = True
        #             if end >= interval[1]:
        #                 interval[1] = end
        #         elif interval[0] < start and start < interval[1] or interval[0] == start and start == interval[1]:
        #             isStart = True
        #             if end >= interval[1]:
        #                 interval[1] = end

        #         out.append(interval)    
        #     else:
        #         start, end = out.pop()
        #         if end >= interval[1]:
        #             interval[1] = end
        #             if start <= interval[0]:
        #                 interval[0] = start
        #         elif end == interval[0] or end < interval[1] and end > interval[0]:
        #             interval[0] = start
        #         else:
        #             out.append([start,end])
                    
        #         out.append(interval)
        #     print(out)

        # return out if out else [newInterval]

        out = []
        start, end = newInterval
        for interval in intervals:

            if interval[1] < start:
                out.append(interval)

            elif interval[0] > end:
                out.append([start, end])
                return out + intervals[intervals.index(interval):]
            else:
                start = min(start,interval[0])
                end = max(end, interval[1])

        out.append([start,end])
        return out
