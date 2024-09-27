class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # size = len(s)
        # matrix = [[" " for _ in range(size//2)] for _ in range(numRows)]

        # maxCounter = numRows // 2
        # counter = numRows
        # spaceCounter = 0

        # i = 0
        # for j in range(size//2):
        #     for i in range(numRows):
        #         if counter > 0:
        #             matrix[i][j] = s[i]
        #             counter -= 1
        #             i += 1
        #         else:
        #             if spaceCounter == maxCounter:
        #                 counter = numRows
        #             spaceCounter += 1
                    
        
        # newStr = []
        # for i in range(numRows):
        #     for j in range(size//2):
        #         newStr.append(matrix[i][j])

        # return "".join(newStr)
                
        if numRows == 1:
            return s

        rows = ['' for _ in range(min(numRows, len(s)))]
        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row +=1 if going_down else -1

        return ''.join(rows)