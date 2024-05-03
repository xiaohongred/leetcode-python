import heapq


class SeatManager:

    def __init__(self, n: int):
        self.unres = [i for i in range(1, n + 1)]
        heapq.heapify(self.unres)

    def reserve(self) -> int:
        s = heapq.heappop(self.unres)
        return s

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unres, seatNumber)
        return


if __name__ == '__main__':
    n = 100
    obj = SeatManager(n)

    param_1 = obj.reserve()
    print(param_1)
    obj.unreserve(param_1)
