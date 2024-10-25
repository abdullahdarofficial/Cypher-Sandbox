class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        # strs = 'abc'
        # result = []
        # def makecomb(s, curr):
        #     print(curr)
        #     if len(curr) < n:
        #         for char in s:
        #             if curr and char != curr[-1]:
        #                 makecomb(s, curr + char)
        #             elif not curr:
        #                 makecomb(s, curr + char)
        #     else:
        #         result.append(curr)

        # makecomb(strs, "")
        # result.sort()

        # if len(result) >= k:
        #     return result[k-1]
        # else:
        #     return ""

        chars = "abc"

        total = 3 * ( 2 ** (n - 1))

        if k > total:
            return ""

        result = []

        first = (k-1)//(2**(n-1))
        result.append(chars[first])

        k = (k - 1) % (2 ** (n-1))

        for i in range(n - 1):
            prev_char = result[-1]

            remaining_chars = [c for c in chars if c != prev_char]
            next_char_index = k // (2 ** (n-i-2))
            result.append(remaining_chars[next_char_index])
            k %= (2 ** (n-i-2))

        return ''.join(result)
