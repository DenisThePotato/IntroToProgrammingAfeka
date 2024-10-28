#-------------------- Part 1- q3 --------------------
cost = int(input("Desired furniture cost: "))
distance = int(input("Distance from shop (km): "))
floor = int(input("Floor number: "))
weight = int(input("Desired furniture weight: "))
print(f"Item cost: {cost}.")
print(f"Delivery drive cost: {distance * 5}.")
print(f"Delivery to floor extra cost: {floor * weight}.")
print(f"Recommended tip for the delivery workers: {cost * 0.1}.")
print(f"Total cost: {cost * 1.1 + distance * 5 + floor * weight}.")

#-------------------- Part 3- q5 --------------------
bagrut = float(input("Bagrut grade: "))
psychometry = int(input("Psychometry grade: "))
psychometryMath = int(input("Math psychometry grade: "))
psychometryEnglish = int(input("English psychometry grade: "))
if bagrut >= 102 or (psychometry >= 700 and psychometryMath >= 145 and psychometryEnglish >= 120):
    print("You're eligible for enrollment into the Liliput college.")
elif ((psychometry * 0.8) + (bagrut / 1.2)) >= 600:
    print("You're eligible for enrollment into the Liliput college.")
else:
    print("You're not eligible for enrollment into the Liliput college.")
    print("These are your possible courses of action (each will lead to acceptance): ")
    print(f"- Improve your bagrut grades by {102 - bagrut}")
    if psychometry >= 700:
        if psychometryMath < 145 and psychometryEnglish < 120:
            print(f"- Improve your psychometry math grade by {145 - psychometryMath}")
            print(f"As well as the psychometry english grade by {120 - psychometryEnglish}")
        elif psychometryEnglish < 120:
            print(f"- Improve your psychometry english grade by {120 - psychometryEnglish}")
        else:
            print(f"- Improve your psychometry math grade by {145 - psychometryMath}")
    else:
        print(f"- Improve your psychometry grade by {700 - psychometry}")
    print (f"- Improve your bagrut and psychometry mixed grade from {(psychometry * 0.8) + (bagrut / 1.2)} to 600.")
    print("* The formula for calculating the mixed grade is: Psychometry grade * 0.8 + Bagrut grade / 1.2")

#-------------------- Part 3- q6 --------------------
restingHeartRate = int(input("Resting heart rate: "))
week = int(input("Total weeks of working out: "))
if week <= 2:
    print("You should run for 3Km in the next workout.")
elif 3 <= week <= 4:
    if restingHeartRate <= 70:
        print("You should run for 5Km in the next workout.")
    else:
        print("You should run for 3Km in the next workout.")
else:
    if restingHeartRate <= 59:
        print("You should run for 10Km in the next workout.")
    elif 60 <= restingHeartRate <= 70:
        print("You should run for 8Km in the next workout.")
    else:
        print("You should run for 3Km in the next workout.")

#-------------------- Part 3- q7 --------------------
examGrade = int(input("Exam grade: "))
homeworkAverage = int(input("Homework average grade: "))
exercisesSubmitted = int(input("Number of homework exercises submitted: "))
if exercisesSubmitted <= 4:
    print("Your grade: 0.")
elif 5 <= exercisesSubmitted <= 6:
    if examGrade >= 55:
        print(f"Your grade: {0.8 * examGrade + 0.2 * homeworkAverage}.")
    else:
        print(f"Your grade: {examGrade}.")
else:
    if examGrade <= 54:
        if homeworkAverage >= 80:
            if homeworkAverage > examGrade:
                print(f"Your grade: {examGrade * 0.75 + homeworkAverage * 0.25}")
            else:
                print(f"Your grade: {examGrade}")
        else:
            if homeworkAverage > examGrade:
                print(f"Your grade: {examGrade * 0.8 + homeworkAverage * 0.2}")
            else:
                print(f"Your grade: {examGrade}")
    else:
        if homeworkAverage > examGrade:
            print(f"Your grade: {examGrade * 0.7 + homeworkAverage * 0.3}")
        else:
            print(f"Your grade: {examGrade}")

#-------------------- Part 4- q4, q10, q11, q17 --------------------

