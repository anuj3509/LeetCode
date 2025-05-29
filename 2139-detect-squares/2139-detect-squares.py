class DetectSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)     # hashmap for visited points
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1     # a list cannot be a key in python
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        # this loop goes through all the diagonal values
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:    # condition to check if its a diagonal
                continue
            res += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)