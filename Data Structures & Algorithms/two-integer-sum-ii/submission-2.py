class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1


        while left != right:

            # Numbers meet target
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            # Numbers are greater, move right to the left one
            if numbers[left] + numbers[right] > target:
                right -= 1
                continue
            
            # Numbers are less, move left to the right one
            if numbers[left] + numbers[right] < target:
                left += 1
                continue
        
            
        