class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        blocksLen = len(blocks)
        whiteBlockLen = 0
        for i, c in enumerate(blocks):

            left = i - k + 1
            if c == 'W':
                whiteBlockLen += 1
            
            if left < 0:
                continue
            
            ans = min(ans, whiteBlockLen)
            if blocks[left] == 'W':
                whiteBlockLen -= 1
        return ans



if __name__ == "__main__":
    solution = Solution()
    blocks = "WBBWWBBWBW"
    k = 7
    result = solution.minimumRecolors(blocks, k)
    print(result)  # Output: 3

    blocks = "WBWBBBW"
    k = 2
    result = solution.minimumRecolors(blocks, k)
    print(result)  # Output: 0