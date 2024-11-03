class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        # while len(s) > k:
        #     i, j = 0, k
        #     lis = []
        #     while j <= len(s):
        #         lis.append(s[i:j])
        #         i = j
        #         j += k

        #     if j > len(s):
        #         lis.append(s[i:])
            
        #     for sub in lis:
        #         result = sum(int(digit) for digit in sub)
        #         lis.append(str(result))

        #     s = ''.join(lis)
        # return s


        while len(s) > k:
            new = []
            for i in range(0, len(s), k):
                sub = s[i : i+k]
                result = sum(int(digit) for digit in sub)
                new.append(str(result))
            s = ''.join(new)
        return s

            
