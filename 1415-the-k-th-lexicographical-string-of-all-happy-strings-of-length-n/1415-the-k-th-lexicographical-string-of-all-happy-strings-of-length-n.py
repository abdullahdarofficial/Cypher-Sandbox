class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        strs = 'abc'
        result = []
        def makecomb(s, curr):
            print(curr)
            if len(curr) < n:
                for char in s:
                    if curr and char != curr[-1]:
                        makecomb(s, curr + char)
                    elif not curr:
                        makecomb(s, curr + char)
            else:
                result.append(curr)

        makecomb(strs, "")
        result.sort()

        if len(result) >= k:
            return result[k-1]
        else:
            return ""