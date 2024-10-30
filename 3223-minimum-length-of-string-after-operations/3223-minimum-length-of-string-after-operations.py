class Solution:
    def minimumLength(self, s: str) -> int:
        map = Counter(s)
        result = 0
        for char, count in map.items():
            if count % 2 == 0:
                result += 2
            else:
                result += 1
            
        return result
