class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        print(num)
        
        # def nextWonderful(n):
        #     number = list(n)
        #     i = len(number) - 1
        #     heap = []
            
        #     while i > 0:
        #         if number[i] < number[i-1]:
        #             heapq.heappush(heap, number[i])
        #             number.pop()
        #         else:
        #             number[i], number[i-1] = number[i-1], number[i]
        #             break
        #         i -= 1
        #     while heap:
        #         number.append(heapq.heappop(heap))
        #     return ''.join(number)

        # for i in range(k - 1):
        #     num = nextWonderful(num)

        # return nextWonderful(num)

            
                    

        # def nextWonderful(n):
        #     number = list(n)
        #     i = len(number) - 1

        #     while i > 0:
        #         if number[i] > number[i - 1]:
        #             break
        #         i -= 1
            
        #     if i == 0:
        #         return ''.join(number) # no greater permutation found

        #     j = len(number) - 1

        #     while number[j] <= number[i - 1]:
        #         j-=1
            
        #     number[i-1], number[j] = number[j], number[i-1]
        #     number[i:] = reversed(number[i:])
        #     return ''.join(number)

        # for _ in range(k):
        #     num = nextWonderful(num)

        # return num
 

        def nextWonderful(n):
            number = list(n)
            i = len(number) - 1

            while i > 0:
                if number[i] > number[i - 1]:
                    break
                i -= 1
            
            if i == 0:
                return ''.join(number) # no greater permutation found

            j = len(number) - 1

            while number[j] <= number[i - 1]:
                j-=1
            
            number[i-1], number[j] = number[j], number[i-1]
            number[i:] = reversed(number[i:])
            return ''.join(number)

        dest = num
        for _ in range(k):
            dest = nextWonderful(dest)
        org = num
        num = list(num)  # Convert string to list
        swaps = 0
        for i in range(len(num)):
            if num[i] != dest[i]:
                j = i + 1

                while num[j] != dest[i]:
                    j += 1

                while(j > i):
                    num[j], num[j-1] = num[j-1], num[j]
                    j-=1
                    swaps += 1

        return swaps
