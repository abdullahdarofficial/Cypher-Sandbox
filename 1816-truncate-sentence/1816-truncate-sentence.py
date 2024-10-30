class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        lis = s.split(' ')
        return ' '.join(lis[:k])
