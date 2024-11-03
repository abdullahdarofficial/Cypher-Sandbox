class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        i, j = 0, k
        answer = []

        while j <= len(nums):
            # Get the current subarray of length k
            subarray = nums[i:j]
            # Count occurrences of each element
            count = Counter(subarray)

            # Sort the items first by frequency (descending) and then by element value (descending)
            sorted_count = sorted(count.items(), key=lambda item: (-item[1], -item[0]))

            # Calculate the x-sum
            result = 0
            for idx in range(min(x, len(sorted_count))):
                result += sorted_count[idx][0] * sorted_count[idx][1]

            answer.append(result)

            # Move the sliding window
            i += 1
            j += 1

        return answer