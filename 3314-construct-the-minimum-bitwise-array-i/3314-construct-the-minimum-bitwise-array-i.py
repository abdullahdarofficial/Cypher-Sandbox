class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            found = False
            # Start searching from num // 2 to find the smallest ans[i] satisfying the condition
            for candidate in range(num // 2, num):
                if candidate | (candidate + 1) == num:
                    ans.append(candidate)
                    found = True
                    break
            # If no valid candidate was found, append -1
            if not found:
                ans.append(-1)
                
        return ans