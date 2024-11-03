class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        false = 0
        for word in words:
            count = Counter(word)
            for key, _ in count.items():
                if key not in allowed:
                    false += 1
                    break
        return len(words) - false

                    