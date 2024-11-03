class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        news = s.lower()
        count = 0
        for i in range(len(news) - 1):
            if news[i] != news[i+1]:
                count += 1
        return count
        