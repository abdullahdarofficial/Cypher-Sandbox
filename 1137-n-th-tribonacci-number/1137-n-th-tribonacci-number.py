class Solution:
    def tribonacci(self, n: int) -> int:
        

        # def recursive(k):
        #     if k == 0:
        #         return 0
        #     if k == 1 or k == 2:
        #         return 1
            
        #     return recursive(k - 1) + recursive(k - 2) + recursive(k - 3)

        # return recursive(n)

        # with 1 dp
 
        if n == 1 or n == 2:
            return 1
        if n == 0:
            return 0
        t_arr = [0] * (n + 1)
        t_arr[1] = 1
        t_arr[2] = 1
        for i in range(3, n + 1):
            t_arr[i] = t_arr[i - 3] +  t_arr[i - 2] +  t_arr[i - 1]
        return t_arr[-1]