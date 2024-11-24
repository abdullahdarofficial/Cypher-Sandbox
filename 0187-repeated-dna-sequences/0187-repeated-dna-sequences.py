class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # if len(s) < 10: return []

        # result = []
        # for i in range(len(s) - 10):
        #     sub_arr = s[i: i + 10]

        #     if sub_arr in result:
        #         continue

        #     for j in range(i + 1, len(s)):
        #         next_arr = s[j : j + 10]
        #         if next_arr == sub_arr:
        #             result.append(sub_arr)
        #             break

        # return result

        
            

        if len(s) < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 10 + 1):
            substring = s[i : i+10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)
        return list(repeated)