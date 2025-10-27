def get_subsets(nums: list[int]) -> list[list[int]]:

    result = []

    def generate_subsets(
        start: int,
        sub_set: list[int]
    ) -> list[list[int]]:
        print(sub_set)
        result.append(sub_set[:])

        for i in range(start, len(nums)):
            sub_set.append(nums[i])
            generate_subsets(
                i + 1,
                sub_set
            )
            sub_set.pop()
    generate_subsets(0, [])
    return result

# print(get_subsets([1, 2, 3, 4]))
print(get_subsets([1, 2, 3]))
# print(get_subsets([1, 2]))

# get_subsets([1, 2, 3])