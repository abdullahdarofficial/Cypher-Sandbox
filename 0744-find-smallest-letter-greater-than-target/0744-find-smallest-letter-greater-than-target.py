class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # low, high = 0, len(letters) - 1
        # index = 0
        # found = False
        # while low <= high:
        #     mid = (low + high) // 2

        #     if letters[mid] == target:
        #         index = mid
        #         found = True
        #         break
        #     elif letters[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        
        # val = letters[index]
        # if not found:
        #     return letters[0]
        # index += 1
        # while index < len(letters) and val == letters[index]:
        #     index += 1
      
        # return letters[index] if index < len(letters) else letters[0]

        low, high = 0, len(letters) - 1

        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        # After binary search, low points to the smallest letter greater than target
        return letters[low % len(letters)]