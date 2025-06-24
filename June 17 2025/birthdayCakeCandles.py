def birthdayCakeCandles(candles):
    if not candles:
        print(0)
        return
    max_height = 0
    for height in candles:
        if height > max_height:
            max_height = height

    count = 0
    for height in candles:
        if height == max_height:
            count += 1
    print(count)
