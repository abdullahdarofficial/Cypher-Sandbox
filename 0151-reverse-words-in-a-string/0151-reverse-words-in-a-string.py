class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        words = s.split()
        new_str = []
        for index in range(len(words)-1, -1, -1):
            word = words[index].strip()
            new_str.append(word)

        return " ".join(new_str)
