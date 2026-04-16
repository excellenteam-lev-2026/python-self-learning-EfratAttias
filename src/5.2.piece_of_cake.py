def piece_of_cake(prices, optionals=[], **kwargs):
    total_price = 0
    for item, price in prices.items():
        if item not in optionals:
            total_price += (prices[item] * kwargs[item]) / 100
    return total_price
    

if __name__ == "__main__":
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))