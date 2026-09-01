from typing import List
from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        litter_positions = []
        start_pos = None

        # 1. 收集所有关键位置：垃圾 'L' 和起点 'S'
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'L':
                    litter_positions.append((r, c))
                elif classroom[r][c] == 'S':
                    start_pos = (r, c)

        # 没有垃圾要捡
        if not litter_positions:
            return 0

        # 给每个垃圾分配一个编号 (bit)，最多10个垃圾
        litter_index = {pos: i for i, pos in enumerate(litter_positions)}
        target_mask = (1 << len(litter_positions)) - 1  # 比如有3个垃圾，target_mask就是 0b111

        # BFS队列: (行, 列, 剩余能量, 已捡垃圾的位掩码, 步数)
        q = deque()
        q.append((start_pos[0], start_pos[1], energy, 0, 0))

        # visited 记录: (行, 列, 掩码) -> 这个状态下的最大剩余能量
        # 同一个位置、同样的垃圾收集情况，剩余能量越大越好
        visited = {(start_pos[0], start_pos[1], 0): energy}

        while q:
            r, c, cur_energy, mask, steps = q.popleft()

            # 所有垃圾都捡完了！
            if mask == target_mask:
                return steps

            # 四个方向移动
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                # 边界检查
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                cell = classroom[nr][nc]

                # 墙不能走
                if cell == 'X':
                    continue

                # 移动一步，能量-1
                new_energy = cur_energy - 1

                # 如果能量变成负数，说明这一步走不了
                if new_energy < 0:
                    continue

                new_mask = mask
                # 如果是垃圾格子，更新掩码（收集垃圾）
                if cell == 'L':
                    idx = litter_index[(nr, nc)]
                    new_mask = mask | (1 << idx)

                # 如果走到了 'R' 充电站，能量回满
                if cell == 'R':
                    new_energy = energy

                # 状态查重：如果这个状态没访问过，或者这次剩余能量更多，才入队
                state = (nr, nc, new_mask)
                if state not in visited or visited[state] < new_energy:
                    visited[state] = new_energy
                    q.append((nr, nc, new_energy, new_mask, steps + 1))

        # 队列空了还没收集完所有垃圾，说明不可能
        return -1
if __name__ == "__main__":
    solution = Solution()
    classroom = ["S.", "XL"]
    energy = 2
    result = solution.minMoves(classroom, energy)
    print(result)  # Output: 2

    classroom = ["LS", "RL"]
    energy = 4
    result = solution.minMoves(classroom, energy)
    print(result)  # Output: 3


    classroom = ["L.S", "RXL"]
    energy = 3
    result = solution.minMoves(classroom, energy)
    print(result)  # Output: -1

    classroom = ["S", "L", "R", "L"]
    energy = 2
    result = solution.minMoves(classroom, energy)
    print(result)  # Output: 3