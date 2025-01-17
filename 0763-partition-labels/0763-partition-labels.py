class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # org_start, start, end = 0, 0, 0
        # substr = s
        # result = []
        # n = len(s)
        # while start < n:
        #     char = s[start]
        #     for i in range(start, n):
        #         if char == s[i]:
        #             end = max(i, end)
        #     if start == end:
        #         result.append(end + 1 - org_start)
        #         org_start = end + 1
        #     start += 1
            
        # return result

        last_occur = { char : idx for idx, char in enumerate(s)}
        start, end = 0, 0
        result = []

        for idx, char in enumerate(s):
            end = max(end, last_occur[char])
            if idx == end:
                result.append(end + 1 - start)
                start = idx + 1
        return result