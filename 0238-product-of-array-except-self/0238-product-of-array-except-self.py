class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # if not nums:
        #     return []
      
        # product = abs(int(nums[0]/1))
        # prod = abs(int(nums[0]/1))

        # for num in nums:
        #     if num != 0:
        #         product *= num
        #     prod *= num
            

        # for index in range(len(nums)):
        #     if nums[index] != 0:
        #         nums[index] = int(prod / nums[index])
        #     else:
        #         nums[index] = product

        # return nums

        arr = [1 for _ in range(len(nums))]
        product = 1
        print(arr)

        for index in range(0, len(nums) - 1):
            product *= nums[index]
            arr[index + 1] *= product
        product = 1

        print(arr)
        for index in range(len(nums) - 1, 0, -1):
            product *= nums[index]
            arr[index - 1] *= product

        print(arr)

        return arr

        
        