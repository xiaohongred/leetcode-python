class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ['(', '{', '[']:
                st.append(c)
            else:
                if len(st) == 0:
                    return False

                c1 = st.pop()
                if c == ')' and c1 != '(':
                    return False

                if c == '}' and c1 != '{':
                    return False

                if c == ']' and c1 != '[':
                    return False

        if len(st) > 0:
            return False

        return True

    def isValidV2(self, s: str) -> bool:
        st = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                if st and st[-1] == closeToOpen[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

        if len(st) > 0:
            return False

        return True


if __name__ == '__main__':
    s = "[][][][][]{{}}"
    so = Solution()
    a = so.isValid(s)
    print(a)
