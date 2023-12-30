from typing import List

class Solution:
    @staticmethod
    def countNegatives(grid: List[List[int]]) -> int:
        count = 0
        target = 0
        for i in range(len(grid)):
            if grid[i][0] < target:
                count += len(grid[i])
                continue
            if grid[i][-1] > target:
                continue
            print (count)
            left = 0
            right = len(grid[i]) - 1
            while left <= right:
                middle = (left + right) // 2
                if grid[i][middle] == target:
                    count += len(grid[i]) - middle - 1
                    break
                elif grid[i][middle] > target:
                    left = middle + 1
                else:
                    right = middle - 1
            if grid[i][middle] != 0:
                count += len(grid[i]) - left
        return count

    @staticmethod
    def search(nums: List[int], target: int) -> int:    
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1
        
        def search_rotate_index(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                if middle == 0:
                    if nums[1] > nums[0]:
                        return 0
                    else:
                        return 1
                elif middle == len(nums) - 1:
                    if nums[-1] > nums[-2]: 
                        return 0
                    else:
                        return len(nums) - 1
                else:
                    if nums[middle+1] > nums[middle] and nums[middle-1] > nums[middle]:
                        return middle
                    else:
                        if nums[middle] >= nums[0]:
                            left = middle + 1
                        else:
                            right = middle - 1
        
        if nums[0] <= nums[-1]:
            return binary_search(nums, target)
        if nums[0] > nums[-1]:
            rotate_index = len(nums) - search_rotate_index(nums)
            if target > nums[0]:
                return binary_search(nums[:len(nums)-rotate_index], target)
            if target < nums[0]:
                result = binary_search(nums[len(nums)-rotate_index:], target)
                if result != -1:
                    result += len(nums) - rotate_index
                return result
            if target == nums[0]:
                return 0

print (Solution.search([3,5,1], 0)) 