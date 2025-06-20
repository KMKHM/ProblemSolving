class SnapshotArray:
    def __init__(self, length: int):
        self.arr = [0] * length
        self.map = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.map[self.snap_id] = self.arr[:]
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.map[snap_id][index]


arr = SnapshotArray(3)  # [0, 0, 0]
arr.set(0, 5)
snap_id1 = arr.snap()   # snap_id1 = 0
arr.set(0, 6)
val = arr.get(0, 0)  # 5

print(val)
