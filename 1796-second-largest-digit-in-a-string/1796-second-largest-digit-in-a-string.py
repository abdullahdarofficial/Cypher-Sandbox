class Solution:
    def secondHighest(self, s: str) -> int:
        first, second = -1, -1

        for char in s:
            if char.isnumeric():
                num = int(char)
                if num > first:
                    second = first
                    first = num
                elif num > second and num < first:
                    second = num
        return second