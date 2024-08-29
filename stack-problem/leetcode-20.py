class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(",
                       "]": "[",
                       "}": "{"
                       }
        for c in s:
            if c in closeToOpen:  # 如果是闭括号,从栈顶中找对应的开括号,如果匹配，消掉，如果不匹配，返回false
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:  # 如果是开括号，入栈
                stack.append(c)
        return len(stack) == 0


if __name__ == '__main__':
    s = "()"
    solu = Solution()
    a = solu.isValid(s)
    print(a)

    s = "()[]{}"
    a = solu.isValid(s)
    print(a)

    s = "(]"
    a = solu.isValid(s)
    print(a)

    s = "([])"
    a = solu.isValid(s)
    print(a)
