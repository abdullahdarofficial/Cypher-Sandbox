class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge case: If string length is less than or equal to 1, return the length
        if len(s) <= 1:
            return len(s)
        
        left = 0
        max_len = 0
        char_set = set()  # Set to keep track of unique characters in the current window
        
        for right in range(len(s)):
            # If character at `right` is already in the set, move the `left` pointer forward
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the character at `right` to the set and update the max length
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
