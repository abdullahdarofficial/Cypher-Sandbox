class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # if len(s) == 1 and k == 1:
        #     return 1

        # maxsize = 0
        # for i in range(len(s) - k):
        #     for j in range(i + k, len(s) + 1):
        #         substring = s[i : j]
        #         count = Counter(substring)
        #         okay = True
        #         for key, value in count.items():
        #             if value < k:
        #                 okay = False
        #                 break
        #         if okay:
        #             maxsize = max(maxsize, len(substring))
        # return maxsize


        if len(s) < k:
            return 0

        freq = Counter(s)

        for char in s:
            if freq[char] < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
                
        return len(s)