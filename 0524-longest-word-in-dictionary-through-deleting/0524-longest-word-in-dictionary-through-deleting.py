class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def canForm(s, word):
            size = len(word)
            j = 0
            for char in s:
                if j == size:
                    return True
                elif word[j] == char:
                    j += 1 
            return j == size

        index = 0
        while index < len(dictionary):
            if not canForm(s, dictionary[index]):
                dictionary.pop(index)
            else:
                index += 1

        dictionary.sort()
        dictionary.sort(key=lambda x: len(x))

        print(dictionary)
        j = len(dictionary) - 1
        while j > 0:
            if len(dictionary[j]) != len(dictionary[j-1]):
                break
            j-=1
        return dictionary[j] if dictionary else []






        