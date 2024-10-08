class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix) #rows
        n = len(matrix[0]) #cols
        hlevel = 0
        vlevel = 0 

        i = 0
        j = 0
        arr = []
        size = m * n
        while size:

            while j < n - hlevel and size:
                arr.append(matrix[i][j])
                size -= 1
                j += 1
            j-=1
            i +=1
            while i < m - vlevel and size:
                arr.append(matrix[i][j])
                size -= 1
                i += 1
            i-=1
            j-=1
            
            while j >= hlevel and size:
                arr.append(matrix[i][j])
                size -= 1
                j -= 1 
            j+=1
            i-=1
            
            while i > vlevel and size:
                arr.append(matrix[i][j])
                size -= 1
                i -= 1
            i+=1
            j+=1
            hlevel += 1
            vlevel += 1

        return arr