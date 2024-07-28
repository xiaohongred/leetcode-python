class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}  # (i, j) -> number of change

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(word1) and j >= len(word2):
                return 0

            if i >= len(word1):
                return len(word2) - j

            if j >= len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i, j + 1) + 1,  # insert
                          dfs(i + 1, j) + 1,  # delete
                          dfs(i + 1, j + 1) + 1  # replace
                          )
            memo[(i, j)] = res
            return res

        return dfs(0, 0)

    def minDistanceDP(self, word1: str, word2: str) -> int:

        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # 注意， 这里 cache 不能用
        # cache = [[float("inf")] * (len(word2) + 1)] * (len(word1) + 1))
        #  的方式初始化

        # for index in range(len(cache)):
        #     print(cache[index])
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # for index in range(len(cache)):
        #     print(cache[index])
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i][j + 1],  # insert
                        cache[i + 1][j],  # delete
                        cache[i + 1][j + 1]  # replace
                    )
        return cache[0][0]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"

    s = Solution()
    a = s.minDistance(word1, word2)
    print(a)

    a = s.minDistanceDP(word1, word2)
    print(a)
# cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)] 和 cache = [[float("inf")] * (len(word2) + 1)] * (len(word1) + 1)) 的区别

# 在这两个表达式中，它们的区别在于如何创建二维列表（2D list）cache。
#
# 第一个表达式：
#
# python
# Copy code
# cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
# 这种方式会创建一个包含 len(word1) + 1 行，每行都是一个长度为 len(word2) + 1 的列表。每行都是独立的对象，因此修改其中一个元素不会影响其他行。
#
# 第二个表达式：
#
# python
# Copy code
# cache = [[float("inf")] * (len(word2) + 1)] * (len(word1) + 1)
# 这种方式创建的二维列表中，所有行其实是引用了同一个列表对象的副本。换句话说，这种方式实际上创建了 len(word1) + 1 个指向相同内存地址的列表。这意味着，如果你修改了其中一个子列表中的元素，其他所有子列表相同位置的元素也会被修改，因为它们实际上指向的是同一个列表。
#
# 总结：
#
# 使用第一个表达式可以确保每行是独立的对象，修改一个子列表不会影响其他子列表。
# 使用第二个表达式则会导致所有子列表共享相同的引用，可能导致意外的行为，特别是在修改元素时。
# 在大多数情况下，建议使用第一个表达式以避免由于共享引用而引起的潜在问题。
