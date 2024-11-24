class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        def compute_version(s):
            return list(map(int, s.split('.')))

        v1 = compute_version(version1)
        v2 = compute_version(version2)

        max_len = max(len(v1), len(v2))
        v1 += [0] * (max_len - len(v1))
        v2 += [0] * (max_len - len(v2))

        for i in range(max_len):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        return 0