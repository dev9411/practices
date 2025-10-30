# Given a string expression of numbers and operators,
# return all possible results from computing all the different possible ways 
# to group numbers and operators. You may return the answer in any order.

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10

from abc import ABC, abstractmethod
from functools import lru_cache
from typing import List


# --- Operator hierarchy ---
class Operator(ABC):
    @abstractmethod
    def execute(self, val1: int, val2: int) -> int:
        pass

class Add(Operator):
    def execute(self, val1: int, val2: int) -> int:
        return val1 + val2

class Sub(Operator):
    def execute(self, val1: int, val2: int) -> int:
        return val1 - val2

class Mul(Operator):
    def execute(self, val1: int, val2: int) -> int:
        return val1 * val2


# --- Simple Factory ---
def compute(val1: int, val2: int, op: str) -> int:
    ops = {'+': Add(), '-': Sub(), '*': Mul()}
    return ops[op].execute(val1, val2)


# --- Main recursive solver ---
def diffWaysToCompute(expression: str) -> List[int]:
    @lru_cache(None)
    def recurse(expr: str) -> List[int]:
        results = []

        # Split at each operator and combine all possibilities
        for i, char in enumerate(expr):
            if char in "+-*":
                left_results = recurse(expr[:i])
                right_results = recurse(expr[i + 1:])
                for l in left_results:
                    for r in right_results:
                        results.append(compute(l, r, char))

        # Base case: no operator, it's just a number
        if not results:
            results = [int(expr)]

        return results

    return recurse(expression)


# --- Example usage ---
if __name__ == "__main__":
    # print(diffWaysToCompute("2-1-1"))      # [0, 2]
    # print(diffWaysToCompute("2*3-4*5"))    # [-34, -14, -10, -10, 10]
    print(diffWaysToCompute('2-1-1*32-100'))
