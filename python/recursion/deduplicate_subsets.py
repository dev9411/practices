# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

def deduplicate_subsets(nums: list[int]) -> list[list[int]]:
    nums.sort() # sort first for optimised duplicate detection
    result = []
    def subset(path: list[int], start: int):
        result.append(path[:]) # T = O(n)
        for i in range(start, len(nums)): # T = O(2^n)
            if i > start and nums[i] == nums[i-1]: # Pruning duplicates
                continue
            path.append(nums[i]) # Memory: O(n)
            subset(path, i + 1)
            path.pop()
    subset([], 0)
    return result # Output memory: O(2^n)

# Memory - 2^n times n = O(n * 2^n)

print(deduplicate_subsets([1, 2, 3]))
print(deduplicate_subsets([2, 2, 2]))
print(deduplicate_subsets([2, 1, 2]))
