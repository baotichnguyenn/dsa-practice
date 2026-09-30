class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Storing the complement value to target and each indicies of item in num
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = i

        for i in nums: 
            complement = target - i
            if complement in seen:
                return [nums.index(i), nums.index(complement)]
        

            

    

        