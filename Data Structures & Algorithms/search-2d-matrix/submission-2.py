class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return self.binarySearch(row, target)
        return False

    
    def binarySearch(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            #(l + r) // 2 can lead to overflow
            mid = l + (r-l) // 2

            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1 
        return False