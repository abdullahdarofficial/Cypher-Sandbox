class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrome(word):
            size = len(word)
            for i in range(size//2):
                if word[i] != word[size - i - 1]:
                    return False
            return True
        for word in words:
            if isPalindrome(word):
                return word
        return ""

