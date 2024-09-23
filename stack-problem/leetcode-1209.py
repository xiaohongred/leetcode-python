class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # [char, count]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for c, count in stack:
            res += (c * count)
        return res


if __name__ == '__main__':
    s = "abcd"
    k = 2

    solu = Solution()
    a = solu.removeDuplicates(s, k)
    print(a)

    s = "deeedbbcccbdaa"
    k = 3
    a = solu.removeDuplicates(s, k)
    print(a)

    s = "pbbcggttciiippooaais"
    k = 2
    a = solu.removeDuplicates(s, k)
    print(a)
