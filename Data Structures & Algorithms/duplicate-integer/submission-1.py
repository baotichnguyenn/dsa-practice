class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_present = set()

        for x in nums:
            if x in already_present:
                return True
            already_present.add(x)

        return False