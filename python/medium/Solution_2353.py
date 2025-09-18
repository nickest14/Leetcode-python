# 2353. Design a Food Rating System

from typing import List

from heapq import heappush, heappop


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine: dict[str, str] = {}
        self.food_to_rating: dict[str, int] = {}
        self.cuisine_foods: dict[str, list[tuple[int, str]]] = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            if cuisine not in self.cuisine_foods:
                self.cuisine_foods[cuisine] = []
            heappush(self.cuisine_foods[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine: str = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heappush(self.cuisine_foods[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap: list[tuple[int, str]] = self.cuisine_foods[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heappop(heap)


food_ratings = FoodRatings(
    ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
    ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
    [9, 12, 8, 15, 14, 9],
)

print(food_ratings.highestRated("korean"))
print(food_ratings.highestRated("japanese"))
food_ratings.changeRating("sushi", 16)
print(food_ratings.highestRated("japanese"))
food_ratings.changeRating("ramen", 16)
print(food_ratings.highestRated("japanese"))
