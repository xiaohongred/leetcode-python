class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2tmap = {}
        t2smap = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in s2tmap and s2tmap[c1] != c2) or
                    (c2 in t2smap and t2smap[c2] != c1)):
                return False

            s2tmap[c1] = c2
            t2smap[c2] = c1

        return True


if __name__ == '__main__':
    pass
