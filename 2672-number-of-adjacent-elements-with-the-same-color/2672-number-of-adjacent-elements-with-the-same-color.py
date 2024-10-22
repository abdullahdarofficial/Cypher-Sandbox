class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # array = [-1] * n
        # def adjacentColor(arr):
        #     count = 0
        #     for i in range(len(arr) - 1):
        #         if arr[i] == arr[i + 1] and arr[i] != -1:
        #             count += 1
        #     return count
        
        # result = []
        # for query in queries:
        #     index, color = query
        #     array[index] = color
        #     result.append(adjacentColor(array))

        # return result

        arr = [0] * n
        count = 0
        result = []
        for query in queries:
            ind, color = query
            prevColor = arr[ind]
            if ind > 0 and arr[ind - 1] == prevColor and prevColor != 0:
                count -=1
            if ind < n - 1 and arr[ind + 1] == prevColor and prevColor != 0:
                count -= 1

            arr[ind] = color

            if ind > 0 and arr[ind - 1] == color:
                count += 1
            if ind < n - 1 and arr[ind + 1] == color:
                count += 1
            result.append(count)
        return result