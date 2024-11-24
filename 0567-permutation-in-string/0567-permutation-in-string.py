class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        result = []

        def permutation(rem, curr):
            if len(rem) == 0:
                result.append(''.join(curr))
            else:
                for i in range(len(rem)):
                    permutation(rem[:i] + rem[i+1:], curr + [rem[i]])

        permutation(s1, [])
        for i in range(len(s2) - len(s1) + 1):
            subarr = s2[i: i + len(s1)]
            if subarr in result:
                return True  
        return False