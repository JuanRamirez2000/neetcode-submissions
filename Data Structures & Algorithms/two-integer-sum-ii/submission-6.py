class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left != right:
            computed = numbers[left] + numbers[right]
            if computed == target:
                return [left + 1, right + 1]
            if computed < target:
                left += 1
                pass
            if computed > target:
                right -= 1
                pass