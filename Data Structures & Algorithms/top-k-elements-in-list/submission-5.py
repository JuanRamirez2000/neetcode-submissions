class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 0
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_freq)[:k]
