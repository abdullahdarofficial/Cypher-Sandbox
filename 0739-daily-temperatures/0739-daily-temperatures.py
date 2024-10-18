class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        # result = []

        # for i in range(len(temperatures)):
        #     count = 0
        #     currtemp = temperatures[i]
        #     for j in range(i + 1, len(temperatures)):
        #         if currtemp < temperatures[j]:
        #             count += 1
        #             break
        #         else:
        #             count += 1

        #     result.append(count)

        # return result

        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result

        # remove those elements from stack whose temp is less than current temp if some of the
        # temp have not yet found any high temp in future they will remain zero
#The stack serves as a way to keep track of indices whose warmer temperatures have not yet been found

