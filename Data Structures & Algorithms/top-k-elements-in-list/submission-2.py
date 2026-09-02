class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_tracking = {}
        for i in nums:
            if i in count_tracking:
                count_tracking[i] +=1
            else:
                count_tracking[i] =1
        
        if k>len(count_tracking):
            return False
        
        sorted_items = sorted(
        count_tracking.items(),
        key=lambda item: item[1],
        reverse=True
        )

        return [item[0] for item in sorted_items[:k]]
            
        