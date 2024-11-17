class Solution:
    def partitionString(self, s: str) -> int:

        check = set()
        substr = ""
        count = 0
        for char in s:
            if char in check:
                check.clear()
                check.add(char)
                count += 1
                substr = ""
            else:
                check.add(char)
                substr += char
        return count + 1
            

