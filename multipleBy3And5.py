def multipleOf (num):
    sum = 0
    numbers = list(range(1, num))
    for number in numbers:
        if 0 == (number % 3):
            sum += number
        elif 0 == (number % 5):
            sum += number
        else:
            continue
    return sum

print(multipleOf(1000))