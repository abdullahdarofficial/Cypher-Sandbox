class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        
        # def dfs(matrix, i, j, visited):
        #     size = len(matrix)
        #     if i < 0 or i >= size or j < 0 or j >= size or visited[i][j] == True:
        #         return
            
        #     visited[i][j] = True
        #     directions = [[0,1], [1,0], [0,-1], [-1,0]]

        #     for d in directions:
        #         dfs(matrix, i + d[0], j + d[1], visited)
            
        # size = len(isConnected)
        # count = 0
        # visited = [[False for _ in range(size)] for _ in range(size)]

        # for i in range(size):
        #     for j in range(size):
        #         if isConnected[i][j] == 1 and not visited[i][j]:
        #             dfs(isConnected, i, j, visited)
        #             count += 1
        # return count

        def dfs(matrix, i, visited):
            visited[i] = True
            
            for j in range(len(matrix)):
                if matrix[i][j] == 1 and not visited[j]:
                    dfs(matrix, j, visited)
        
        size = len(isConnected)
        visited = [False] * size
        count = 0

        for i in range(size):
            if not visited[i]:   
                dfs(isConnected, i, visited)
                count += 1   

        return count