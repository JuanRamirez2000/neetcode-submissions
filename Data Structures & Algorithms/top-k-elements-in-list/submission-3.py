class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for n in nums:
            if n in freq:
                freq[n] += 1
                continue
            freq[n] = 1

        sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        top_k = list(sorted_dict.keys())[:k]
        return top_k