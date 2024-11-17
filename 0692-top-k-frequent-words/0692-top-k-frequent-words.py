class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        word_count = Counter(words)
    
        # Sort by frequency (descending) and then by word (ascending)
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
        # Extract the top k words
        result = [word for word, _ in sorted_words]
        return result[:k]