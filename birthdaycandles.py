# input: list of ints
# output: num of candles blown out

# ints = candle number which is correlated to its height
# larger num = taller candle
# neice will blow out tallest candles 

# thoughts

# empty result variable
# tallest variable

# loop through the list
# if num > tallest
# result = 0
# tallest = num AND result += 1
# if num == tallest
# result increases by one
# if it's smaller, we keep going

# outside loop
# return result!

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    blown = 0
    tallest = 0

    for candle in ar:
        if candle > tallest:
            blown = 0
            tallest = candle
            blown += 1
        elif candle == tallest:
            blown += 1

    return blown

print(birthdayCakeCandles([3, 2, 1, 3])) #2 bc blow out both 3s!