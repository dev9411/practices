from typing import List

class RainWaterTrap:
    def trap(self, height: List[int]) -> int:
        return self.max_water(height)

    def max_water(self, arr):
        left = 1
        right = len(arr) - 2
        lMax = arr[left - 1]
        rMax = arr[right + 1]

        res = 0
        while left <= right:
            if rMax <= lMax:
                res += max(0, rMax - arr[right])
                rMax = max(rMax, arr[right])
                right -= 1
            else: 
                res += max(0, lMax - arr[left])
                lMax = max(lMax, arr[left])
                left += 1
        return res
