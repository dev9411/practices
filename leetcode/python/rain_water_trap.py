from typing import List

class RainWaterTrap:
    def trap(self, height: List[int]) -> int:
        if self.is_sorted(height):
            return 0
        max_wall_index = height.index(max(height))
        return (
            self.calc_trapped_water(height[:max_wall_index + 1], max_wall_index)
            +
            self.calc_trapped_water(height[max_wall_index:], 0)
        )
    
    def calc_trapped_water(self, height: List[int], max_wall_index: int) -> int:
        if len(height) < 3:
            return 0
        wall_2_index = self.second_max_wall_index(height, max_wall_index)
        
        if max_wall_index + wall_2_index == len(height) - 1:
            return self.calc_volume(height)

        return (
            self.calc_trapped_water(height[:wall_2_index + 1], wall_2_index)
            +
            self.calc_trapped_water(height[wall_2_index:], 0)
        )

    def second_max_wall_index(self, height: List[int], max_wall_index: int) -> int:
        if max_wall_index == 0:
            return len(height) - 1 - height[::-1].index(max(height[1:]))
        else:
            return height.index(max(height[:-1]))
    
    def calc_volume(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        available_area = self.calc_available_area(height)
        if available_area <= 0:
            return 0

        wall1 = 0
        wall2 = len(height) - 1
        occupied_area = sum(height) - height[wall1] - height[wall2]
        return max(0, available_area - occupied_area)
    
    def calc_available_area(self, height: List[int]) -> int:
        wall1 = 0
        wall2 = len(height) - 1
        return min(height[wall1], height[wall2]) * (wall2 - wall1 - 1)

    def is_sorted(self, arr):
        return self.is_sorted_descending(arr) or self.is_sorted_ascending(arr)

    def is_sorted_ascending(self, arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    def is_sorted_descending(self, arr):
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    
