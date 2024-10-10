class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        # result = [0] * len(spells)

        # for i in range(len(spells)):
        #     for j in range(len(potions)):
        #         if spells[i] * potions[j] >= success:
        #             result[i] += 1

        # return result

        potions.sort()
        result = []

        def binarySearch(potions, required):
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= required:
                    right = mid - 1
                else:
                    left = mid + 1
            return left


        for spell in spells:

            required = (success + spell - 1) // spell

            index = binarySearch(potions, required)

            result.append(len(potions) - index)

        return result