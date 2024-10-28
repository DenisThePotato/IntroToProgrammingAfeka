# calculate number % divider
def calculateRemainder(number, divider):
    if abs(number) > abs(divider):
        return calculateRemainder(number - divider, divider)
    elif abs(number) == abs(divider):
        return 0
    else:
        return number

print(calculateRemainder(15, 4))