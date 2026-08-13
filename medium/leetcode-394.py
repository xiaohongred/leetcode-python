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

    def decodeStringV2(self, s: str) -> str:
        num_stack = []
        str_stack = []

        cur_num = 0
        cur_str = ""

        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)

            elif c == '[':
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                cur_num = 0
                cur_str = ""
            elif c != ']':  # 字母
                cur_str += c
            else:  # 右括号
                repeat = num_stack.pop()
                prev_str = str_stack.pop()

                cur_str = prev_str + cur_str * repeat
        return cur_str


if __name__ == '__main__':
    s = "3[a]2[bc]"
    solu = Solution()
    a = solu.decodeString(s)
    print(a)

    s = "3[a2[c]]"
    a = solu.decodeStringV2(s)
    print(a)

    s = "2[abc]3[cd]ef"
    a = solu.decodeStringV2(s)
    print(a)
