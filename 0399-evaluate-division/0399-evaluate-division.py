# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
#         mapping = {}

#         size = len(equations)
#         variable = set()
#         for i in range(size):
#             # Store tuples in the dictionary instead of lists
#             mapping[(equations[i][0], equations[i][1])] = values[i]
#             variable.add(equations[i][0])
#             variable.add(equations[i][1])

#         result = []
#         for query in queries:
#             first, second = query
#             if first not in variable and second not in variable:
#                 result.append(-1.0)
#             elif (first, second) in mapping:
#                 result.append(mapping[(first, second)])
#             elif (second, first) in mapping:
#                 result.append(1 / mapping[(second, first)])
#                 mapping[(first, second)] = result[-1]
#             else:
#                 isFound = False
#                 for var in variable:
#                     if var != first and var != second and (first, var) in mapping and (var, second) in mapping:
#                         result.append(mapping[(first, var)] / mapping[(var, second)])
#                         mapping[(first, second)] = result[-1]
#                         isFound = True
#                         break
#                 if not isFound:
#                     result.append(-1.0)

#         return result


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        # graph = defaultdict(dict)

        # for (a,b), value in zip(equations, values):
        #     graph[a][b] = value
        #     graph[b][a] = 1/value

        
        # def dfs(start, end, visited):
        #     if start not in graph or end not in graph:
        #         return -1.0
        #     if start == end:
        #         return 1.0
            
        #     visited.add(start)

        #     for neighbor, value in graph[start].items():
        #         if neighbor not in visited:
        #             res = dfs(neighbor, end, visited)
        #             if res != -1.0:
        #                 return res * value

        #     return -1.0

        # result = []
        # for start, end in queries:
        #     result.append(dfs(start, end, set()))
        # return result

        
        
        graph = defaultdict(dict)

        for (a,b) , value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1/value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)

            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return res * value

            return -1.0

        result = []
        for start, end in queries:
            result.append(dfs(start, end, set()))
        return result