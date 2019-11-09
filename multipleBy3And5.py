
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def multipleOf (num):
    sum = []
    for x in range(1, num):
        if 0 == x % 3 or 0 == x % 5:
            sum.append(x)
    return sum

print(sum(multipleOf(1000)))