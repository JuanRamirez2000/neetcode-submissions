from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n_dict = defaultdict(int)

        for n in nums:
            n_dict[n] += 1

        n_dict_sorted = sorted(n_dict.items(), key = lambda item: item[1], reverse = True)
        ans = []
        for idx in range(k):
            ans.append(n_dict_sorted[idx][0])
        return ans