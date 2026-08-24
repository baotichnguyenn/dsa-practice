class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Storing the complement value to target and each indicies of item in num
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        

            

    

        