class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        new = sorted(list(counts.items()), reverse=True, key=lambda x: x[1])
        result = []
        for num in new[:k]:
            result.append(num[0])
        return(result)