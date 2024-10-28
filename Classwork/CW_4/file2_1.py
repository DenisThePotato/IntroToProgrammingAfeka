timeInMinutes = int(input("certain amount of minutes: "))
hours = 0
minutes = 0
while timeInMinutes - 60 >= 0:    #gets us the amount of hours
    hours += 1
    timeInMinutes -= 60
hours = hours % 24
minutes = timeInMinutes
if minutes < 10:
    print(f"The time is {hours}:0{minutes}")
else:
    print(f"The time is {hours}:{minutes}")
