class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0:
            return []

        results = []

        def backtracking(index, combinations):
            if index == len(digits):
                results.append(combinations)
                return

            for letter in mapping[digits[index]]:
                backtracking(index + 1, combinations + letter)

        backtracking(0, "")
        return results
