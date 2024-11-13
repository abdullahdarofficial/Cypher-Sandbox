class Solution:
    def longestPalindrome(self, s: str) -> str:
        # def check(st):
        #     n = len(st)
        #     for i in range(n//2):
        #         if st[i] != st[n-1-i]:
        #             return False
        #     return True
        # if not s:
        #     return 0
        # maxstr = s[0]
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if check(s[i:j+1]) and len(maxstr) < len(s[i:j+1]):
        #             maxstr = s[i:j+1]
        # return maxstr
                    

        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _ in range(n)]
        start, maxlen = 0, 1

        # all elements itself has palindrome
        for i in range(n):
            dp[i][i] = True

        # if any two consecutive elements are same
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start, maxlen = i, 2
        # now from 3 elements to complete string
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start, maxlen  = i, length

        return s[start : start + maxlen]

        