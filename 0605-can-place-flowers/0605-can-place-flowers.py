class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if not flowerbed:
            return n == 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return n == 0
            else:
                return n == 1 or n == 0
        count = 0
        i = 0

        while i < len(flowerbed) and count < n:
            if flowerbed[i] == 0:
                if i > 0 and flowerbed[i - 1] == 0 and i < (len(flowerbed) - 1) and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif i == 0 and flowerbed[i + 1] == 0 :
                    count += 1
                    flowerbed[i] = 1
                elif (i == (len(flowerbed) - 1) and flowerbed[i-1] == 0):
                    count += 1
                    flowerbed[i] = 1
            print(count)
                
            i+=1
        
        return count >= n