class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the potential prefix
        prefix = strs[0]
        
        for string in strs[1:]:
            # Compare prefix with each string and reduce it
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
                
            if not prefix:
                break
        
        return prefix
        