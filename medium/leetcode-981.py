class TimeMap:

    def __init__(self):
        self.keyTimeStampVal = {}  # key=string, value=list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyTimeStampVal.keys():
            self.keyTimeStampVal[key].append([value, timestamp])
            return
        self.keyTimeStampVal[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyTimeStampVal.keys():
            return ""

        valList = self.keyTimeStampVal[key]
        # for i in range(len(valList) - 1, -1, -1):
        #     if valList[i][1] <= timestamp:
        #         return valList[i][0]

        l, r = 0, len(valList) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if valList[m][1] <= timestamp:
                res = valList[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == '__main__':
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    timestamp = 1
    a = timeMap.get("foo", 1)
    print(a)
