class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = []

        self.tm[key].append([value, timestamp])
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ''
        ret = None
        for item in self.tm[key]:
            if timestamp >= item[1]:
                ret = item
        return ret[0] if ret is not None else ''

    def getV2(self, key: str, timestamp: int) -> str:  # 二分法查找
        if key not in self.tm:
            return ''
        ret = ''
        l, r = 0, len(self.tm[key]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            curItem = self.tm[key][mid]
            if curItem[1] > timestamp:
                r = mid - 1
            elif curItem[1] <= timestamp:
                ret = curItem[0]
                l = mid + 1
        return ret


if __name__ == '__main__':
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    a = tm.get("foo", 1)
    print(a)

    a = tm.get("foo", 3)
    print(a)
    tm.set("foo", "bar2", 4)
    a = tm.get("foo", 4)
    print(a)
    a = tm.get("foo", 5)
    print(a)
