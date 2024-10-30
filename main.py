score = int(input("grade:"))

if score >= 90:
    print("Your grade is an A")

elif score >= 80 and score < 90:
    print("Your grade is a B")

elif score >= 70 and score < 80:
    print("Your grade is a C")

elif score >= 60 and score < 70:
    print("Your grade is a D")

else:
    print("Your grade is a F")
