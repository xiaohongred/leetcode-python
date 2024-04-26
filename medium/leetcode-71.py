class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)


if __name__ == '__main__':
    path = "/a/./b/../../c/"
    s = Solution()
    a = s.simplifyPath(path)
    print(a)
