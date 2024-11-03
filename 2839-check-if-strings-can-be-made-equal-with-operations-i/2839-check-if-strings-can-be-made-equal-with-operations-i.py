class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        size = len(s1)
        lis = list(s1)
        for i in range(size - 2):
            if lis[i] != s2[i]:
                lis[i], lis[i+2] = lis[i+2], lis[i]
        
        print(s1)
        print(s2)
        print(lis)
        s1 = ''.join(lis)
        print(s1)
        return s1 == s2


