class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # # .upper()
        # # .lower()

        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # res = set()
        # news = s.lower()
        # for char in news:
        #     if char in vowels:
        #         res.add(char)
        # lis1 = list(res)
        # lis1.sort()
        # lis2 = list(lis1)
        # lis2.reverse()

        # for ind in range(len(s)):
        #     if s[ind] in lis1:
        #         index = lis1(s[ind]).index()
        #         if s[ind].isUpper():
        #             s[ind] = lis2[index].upper()
        #         else:
        #             s[ind] = lis2[index].lower()

        # return s

        vowels = "aeiouAEIOU"

        s_list = list(s)

        vowel_indices = [i for i, char in enumerate(s_list) if char in vowels]

        vowels_in_s = [s_list[i] for i in vowel_indices][::-1]

        for index, vowel in zip(vowel_indices, vowels_in_s):
            s_list[index] = vowel

        return ''.join(s_list)

            

