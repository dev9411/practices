# BST Sequences: A binary search tree was created by traversing through an array 
# from left to right and inserting each element. Given a binary search tree with distinct 
# elements, print all possible arrays that could have led to this tree.

def weave(list1: list[int], list2: list[int]) -> list[list[int]]:
    result = []
    temp = []

    def dfs(i: int, j: int):
        if i == len(list1) and j == len(list2):
            result.append(temp[:])
            return
        if i < len(list1):
            temp.append(list1[i])
            dfs(i + 1, j)
            temp.pop()
        if j < len(list2):
            temp.append(list2[j])
            dfs(i, j + 1)
            temp.pop()

    dfs(0, 0)
    return result

a = [1,2,3]
b = [4,5,6]
print(weave(a, b))

# print(weave([1,2], [3,4]))
