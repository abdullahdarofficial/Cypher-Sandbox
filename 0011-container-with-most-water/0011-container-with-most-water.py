class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # i = 0
        # j = len(height) - 1
        # max_water = 0
        # while i < j:
        #     max_water = max(((j - i) * (min(height[i], height[j]))), max_water)
        #     if height[i] < height[j]:
        #         i+=1
        #     else:
        #         j-=1
        # return max_water









        start = 0
        end = len(height) - 1
        water = 0

        while start < end:
            water = max(water, ((end - start) * min(height[start], height[end])))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        
        return water







