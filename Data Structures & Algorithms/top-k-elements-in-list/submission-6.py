from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1
        
        
        sorted_dict = {k: v for k,v in sorted(seen.items(), key=lambda item: item[1], reverse=True)}

        return list(sorted_dict.keys())[:k]