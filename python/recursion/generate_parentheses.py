# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


from typing import List


def generate_parentheses(n: int) -> List[str]:
    res = []

    def backtrack(curr: str, open_count: int, close_count: int): # Times called: O(Cn) calls
        if len(curr) == 2 * n:
            res.append(curr) # Output memory Space: O(Cn)
            return
        if open_count < n:
            backtrack(curr + '(', open_count + 1, close_count) # Operation memory Space: O(n)
        if close_count < open_count: # creates a matching closed braces for each open
            backtrack(curr + ')', open_count, close_count + 1) # Operation memory Space: O(n)

    backtrack('', 0, 0)
    return res

# print(generate_parentheses(1))
# print(generate_parentheses(2))
# print(generate_parentheses(3))
# print(len(generate_parentheses(5)))
print(len(generate_parentheses(8)))