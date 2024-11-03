class Solution:
    def secondHighest(self, s: str) -> int:
        first, second = -1, -1

        for char in s:
            if char.isnumeric():
                if int(char) > first:
                    second = first
                    first = int(char)
                elif int(char) > second and int(char) < first:
                    second = int(char)
        return second