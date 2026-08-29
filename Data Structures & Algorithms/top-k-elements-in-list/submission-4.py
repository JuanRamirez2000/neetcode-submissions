class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq.keys():
                freq[n] += 1
            else:
                freq[n] = 0

        val_based = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        return list(val_based.keys())[:k]