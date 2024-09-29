class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        newStr = []
        size = min(len(str1), len(str2))

        for i in range(size):
            if str1[i] == str2[i]:
                if len(newStr) > 0:
                    if str1[i] != newStr[0]:
                        newStr.append(str1[i])
                    else:
                        break
                else:
                    newStr.append(str1[i])
            else:
                break
        
        new = "".join(newStr)

        def can_form(s: str, x: str) -> bool:
            if len(x) == 0:
                return False
            if len(s) % len(x) != 0:
                return False
            # Repeat x and check if it equals s
            return (x * (len(s) // len(x))) == s

        return new  if (can_form(str1, new) and can_form(str2, new)) else ""
