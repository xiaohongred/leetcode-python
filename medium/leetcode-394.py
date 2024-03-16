class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(subStr * int(k))

        return "".join(stack)


if __name__ == '__main__':
    s = "3[a]2[bc]"
    solu = Solution()
    a = solu.decodeString(s)
    print(a)
