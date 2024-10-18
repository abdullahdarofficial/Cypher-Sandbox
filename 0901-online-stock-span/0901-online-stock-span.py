class StockSpanner:

    def __init__(self):
        # self.arr = []  # Initialize an empty list to hold the prices
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        # count = 1  # Start count at 1 for the current price
        # idx = len(self.arr) - 1  # Start from the last index

        # while idx >= 0:
        #     if self.arr[idx] <= price:  # If the previous price is less than or equal to current price
        #         count += 1  # Increase the span count
        #         idx -= 1  # Move to the previous day
        #     else:  # If the previous price is greater
        #         break  # End the span count

        # self.arr.append(price)  # Append the current price to the list
        # return count  # Return the span count


        count = 1

        while self.prices and self.prices[-1][0] <= price:
            count += self.spans.pop()
            self.prices.pop()

        self.prices.append((price,count))
        self.spans.append(count)
        return count
