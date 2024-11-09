class Solution:
    def trailingZeroes(self, n: int) -> int:
        curr_count = 0
        total_count = 0
        i = 1
        
        while True:
            curr_count = n//(5**i)
            if curr_count == 0:
                break
            total_count += curr_count
            i+=1
        return total_count
        