class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                # Reduce the prefix size
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix