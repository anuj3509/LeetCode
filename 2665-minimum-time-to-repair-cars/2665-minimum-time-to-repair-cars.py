class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def suffTime(ranks, cars, time):
            cars_done = 0
            for r in ranks:
                cars_done += int(sqrt(time / r))
            return (cars_done >= cars)


        # Binary Search approach
        # worker with the LOWEST rank can repair the car FASTEST
        l = 1
        r = min(ranks) * cars * cars
        res = 0
        while l <= r:
            m = (l + r) // 2
            if suffTime(ranks, cars, m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res