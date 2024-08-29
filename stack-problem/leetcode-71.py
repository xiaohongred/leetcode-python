class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""  # 保存上一个 / 到当前遇到的 / 之间的字符串
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":  # cur 为空，或者为 .  就可以忽略，不需要入栈，否则就需要入栈
                    stack.append(cur)
                cur = ""  # 遇到了一个 / 对 cur 清零
            else:
                cur += c  # 字符不是 / , 加入到 cur
        return "/" + "/".join(stack)


if __name__ == '__main__':
    path = "/home/"
    s = Solution()
    a = s.simplifyPath(path)
    print(a)

    path = "/home//foo/"
    a = s.simplifyPath(path)
    print(a)

    path = "/home/user/Documents/../Pictures"
    a = s.simplifyPath(path)
    print(a)

    path = "/../"
    a = s.simplifyPath(path)
    print(a)

    path = "/.../a/../b/c/../d/./"
    a = s.simplifyPath(path)
    print(a)
