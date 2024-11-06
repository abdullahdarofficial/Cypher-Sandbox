class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(s,n1,n2):
            if (n1 + n2) > 2 * n or n2 > n1:
                return
            if n1 == n2 and n1 + n2 ==  2*n:
                result.append(s)
            else:
                options = "()"
                for option in options:
                    if option == '(':
                        backtrack(s + option, n1 + 1, n2)
                    else:
                        backtrack(s + option, n1, n2 + 1)
        
        backtrack("", 0,0)
        return result
