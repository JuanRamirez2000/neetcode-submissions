class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        candidate_row = []

        for row in matrix:
            if target <= row[-1]:
                candidate_row = row
                break
        
        left, right = 0, len(candidate_row) - 1


        while left <= right:
            mid_index = left + ((right - left) // 2)

            if candidate_row[mid_index] > target:
                right = mid_index - 1

            elif candidate_row[mid_index] < target:
                left = mid_index + 1

            else:
                return True
        return False