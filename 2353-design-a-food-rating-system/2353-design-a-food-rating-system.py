class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        for index, foodd in enumerate(self.foods):
            if foodd == food:
                self.ratings[index] = newRating
            

        

    def highestRated(self, cuisine: str) -> str:
        currMax = -1
        food = ''
        for index, cus in enumerate(self.cuisines):
            if cus == cuisine:
                if currMax < self.ratings[index] or (currMax == self.ratings[index] and food > self.foods[index]):
                    food = self.foods[index]
                    currMax = self.ratings[index]
        return food



        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)