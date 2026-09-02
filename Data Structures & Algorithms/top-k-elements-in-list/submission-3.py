class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # buckets[frequency] = numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # Collect from highest frequency to lowest
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result