class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0 and len(s) == 0 :
            return True
        if len(s) > len(t) or len(t) == 0 :
            return False
        if len(s) == 0:
            return True

        index = 0
        size = len(s)
        for char in t:
            if s[index] == char:
                index += 1
            if index == size:
                return True
        return False