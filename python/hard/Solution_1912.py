# 1912. Design Movie Rental System

from typing import List
from collections import defaultdict
from bisect import insort, bisect_left


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.store: dict[tuple[int, int], int] = defaultdict(int)
        self.films: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.rental: set[tuple[int, int, int]] = set()

        for shop, movie, price in entries:
            self.store[(shop, movie)] = price
            insort(self.films[movie], (price, shop))

    def search(self, movie: int) -> List[int]:
        return list(map(lambda x: x[1], self.films[movie][:5]))

    def rent(self, shop: int, movie: int) -> None:
        price = self.store[(shop, movie)]
        idx = bisect_left(self.films[movie], (price, shop))
        self.films[movie].pop(idx)
        self.rental.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.store[(shop, movie)]
        insort(self.films[movie], (price, shop))
        self.rental.discard((price, shop, movie))

    def report(self) -> List[List[int]]:
        report_stores = sorted(self.rental)[:5]
        return list(map(lambda x: (x[1], x[2]), report_stores))


router = MovieRentingSystem(
    3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
)
print(router.search(1))
router.rent(0, 1)
router.rent(1, 2)
print(router.report())
router.drop(1, 2)
print(router.search(2))
