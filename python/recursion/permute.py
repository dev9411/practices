def permute(nums: list[int]) -> list[list[int]]:
    return backtrack([], nums, [])

def backtrack(path: list[int], remaining: list[int], result: list[list[int]]) -> list[list[int]]:
    if not remaining:
        result.append(path)

    for i in range(len(remaining)):
        backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:], result)

    return result

def permute_2(nums: list[int]) -> list[list[int]]:
    result = [[]]

    for num in nums:
        new_result = []
        for path in result: # [0]
            for i in range(len(path) + 1): # i -> 0, 1
                new_result.append(path[:i] + [num] + path[i:])
        print(new_result)
        result = new_result
        print(result)

    return result

# permute([1])
# print(permute([1]))
# permute([0])
# print(permute([0]))
# permute([2])
# print(permute([2]))
# permute([1, 2])
# print(permute([1, 2]))
# permute([0, 2])
# print(permute([0, 2]))
# print(permute([0, 1, 2]))
print(permute_2([0, 1, 2]))
