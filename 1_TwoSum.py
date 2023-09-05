def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
print(two_sum([2, 7, 11, 15], 26))


# Implementing Binary Search for a more efficient solution 
# to the Two Sum problem.

def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2 # Calculate the middle index

        if arr[mid] == target:
            return mid # Elem found, return its index
        elif arr[mid] < target:
            left = mid + 1 # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half
    
    return -1 # Target not found in the array

def efficient_two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        pair = binary_search(nums, target - nums[i])
        if pair != -1:
            return [i, pair]

print(efficient_two_sum([2, 7, 11, 15], 26))