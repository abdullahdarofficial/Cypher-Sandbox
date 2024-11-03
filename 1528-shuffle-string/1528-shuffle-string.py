class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restored = [''] * len(s)
        for char, index in zip(s, indices):
            restored[index] = char
        return ''.join(restored)