class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # def checkPalindromeOdd(idx):
        #     i = 0
        #     while (idx - i) >= 0 and (idx + i) < len(s):
        #         if s[idx-i] != s[idx + i]:
        #             return None
        #         i+=1
        #     print(idx, i)
        #     i-=1
        #     print(idx, i)
        #     print(s[(idx - i) : (idx + i + 1 )])
        #     return s[(idx - i) : (idx + i + 1 )]

        # def checkPalindromeEven(idx1, idx2):
        #     i = 0
        #     while (idx1 - i) >= 0 and (idx2 + i) < len(s):
        #         if s[idx1 - i] != s[idx2 + i]:
        #             return None
        #         i+=1
        #     print(idx, i)
        #     i-=1
        #     print(idx, i)
        #     print(s[(idx - i) : (idx + i + 1 )])
        #     return s[(idx - i) : (idx + i + 1 )]

            
        # result = []
        # for idx in range(1, len(s) - 1):
        #     ans = checkPalindromeOdd(idx)
        #     if ans: 
        #         result.append(ans)
        # for idx in range(0, len(s) - 1):
        #     print("Even", idx)
        #     ans = checkPalindromeEven(idx, idx + 1)
        #     if ans: 
        #         result.append(ans)
        
        # return max(result) if result else None


        # # Expanding around centers

        # if len(s) == 1:
        #     return s

        # def checkPalindromeOdd(idx):
        #     i = 0
        #     while (idx - i) >= 0 and (idx + i) < len(s):
        #         if s[idx - i] != s[idx + i]:
        #             break
        #         i+=1
        #     i-=1
        #     return s[(idx - i) : (idx + i + 1)]

        # def checkPalindromeEven(idx1, idx2):
        #     i = 0
        #     while(idx1 - i) >= 0 and (idx2 + i) < len(s):
        #         if s[idx1 - i] != s[idx2 + i]:
        #             break
        #         i += 1
        #     i -= 1
        #     return s[(idx1 - i) : (idx2 + i + 1)]

        # result = ""

        # for idx in range(len(s)):
        #     odd_palindrome = checkPalindromeOdd(idx)
        #     even_palindrome = checkPalindromeEven(idx, idx + 1)
        #     result = max(result, even_palindrome, odd_palindrome, key = len)

        # return result


        # Dynamic programming approach

        n = len(s)

        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]

        start, max_len = 0, 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                start, max_len = i, 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, max_len = i, length

        return s[start:start + max_len]


        