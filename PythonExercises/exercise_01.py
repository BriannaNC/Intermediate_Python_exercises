#Aida
#Zainab
#Sofia
grade = int(input("Enter grade from 0 to 100: "))
if grade >=90 and grade<=100:
    print("A")
elif grade <90 and grade >=80:
    print("B")
elif grade <80 and grade >=70:
    print("C")
elif grade <70 and grade >=60:
    print("D")
elif grade <60 and grade >=0:
    print("F")
else:
    print("Invalid grade")