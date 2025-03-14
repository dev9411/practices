from typing import List

class RainWaterTrap:
    def trap(self, height: List[int]) -> int:
        i = 1
        n = len(height)
        self.trapped_volume = [0] * n
        self.height_ranks = [-1]
        self.blocks = [0] * n
        self.current_max_index = 0
        self.previous_max_index = 0

        while i < n:
            while i < n and height[i] <= height[i - 1]:
                self.height_ranks.append(i - 1)
                self.blocks[i] = height[i] + self.blocks[i - 1]
                self.trapped_volume[i] = self.trapped_volume[i - 1]
                i += 1

            if i >= n:
                break

            j = i - 1
            while height[i] > height[self.height_ranks[j]]:
                if self.height_ranks[j] == -1:
                    break
                j = self.height_ranks[j]
                
            self.height_ranks.append(self.height_ranks[j])
            if self.height_ranks[i] == -1:
                self.blocks[i] = 0
                self.previous_max_index = self.current_max_index
                self.current_max_index = i
            else:
                self.blocks[i] = self.blocks[i - 1] + height[i]

            wall2 = self.previous_max_index if self.height_ranks[i] == -1 else self.height_ranks[i]
            self.trapped_volume[i] = self.trapped_volume[wall2] + self.calc_volume(i, height)
            i += 1
        return self.trapped_volume[n-1]

    def calc_volume(self, i, height):
        wall1 = i
        wall2 = self.previous_max_index if self.height_ranks[i] == -1 else self.height_ranks[i]
        max_volume = min(height[wall1], height[wall2]) * (wall1 - wall2 - 1)
        if max_volume <= 0:
            return 0
        return max_volume - self.blocks[i - 1] + self.blocks[wall2]
            
