
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # If the list is empty
            return ""
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for s in strs[1:]:
            while not s.startswith(prefix):  # Check if current string starts with the prefix
                prefix = prefix[:-1]  # Reduce the prefix length
                if not prefix:  # If prefix becomes empty
                    return ""
        return prefix