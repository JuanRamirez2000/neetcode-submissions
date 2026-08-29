class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Two pointers approach
        left, right = 0, len(nums) - 1


        while left <= right:

            ## (left + right) // 2 can be an overflow 
            mid_index = left + ((right - left) // 2)

            # left 
            # if the number is on the left then move right pointer to left of middle
            if nums[mid_index] > target:
                right = mid_index - 1

            # right
            # if the number is on the right then move left pointer to the right
            elif nums[mid_index] < target:
                left = mid_index + 1

            # if the number is not on the right or on the left then it should be in the middle
            # this only works because we find left == right
            # if left !== right then the number isnt in there
            else:
                return mid_index
        return -1