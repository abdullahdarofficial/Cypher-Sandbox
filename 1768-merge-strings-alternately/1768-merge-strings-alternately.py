class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        size = min(len(word1), len(word2))
        word = []
        for i in range(size):
            word.append(word1[i])
            word.append(word2[i])
        if size < len(word1):
            word.append(word1[size:])
        elif size < len(word2):
            word.append(word2[size:])
        return "".join(word)            
