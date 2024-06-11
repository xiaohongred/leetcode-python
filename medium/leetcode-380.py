import random


class RandomizedSet:

    def __init__(self):
        self.maps = {}
        self.lists = []

    def insert(self, val: int) -> bool:
        if val in self.maps.keys():
            return False
        self.maps[val] = len(self.lists)
        self.lists.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.maps.keys():
            index = self.maps[val]
            lastVal = self.lists[-1]
            self.lists[index] = lastVal
            self.lists.pop()
            self.maps[lastVal] = index
            del self.maps[val]  # 放在最后，处理列表中只有一个数时的情况
            return True
        return False

    def getRandom(self) -> int:
        i = random.randint(0, len(self.lists) - 1)
        return self.lists[i]
