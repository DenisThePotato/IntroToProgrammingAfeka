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