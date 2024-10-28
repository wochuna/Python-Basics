maths = float(input("Enter Maths marks:"))
eng = float(input("Enter English marks:"))
kis = float(input("Enter Kiswahili marks:"))
geo = float(input("Enter Geography marks:"))

# A grading system
# 0 - 39 D
# 40 - 59 C
# 60 - 79 B
# 80 - 100 A

total = maths + eng + kis + geo

avg = total / 4

print(avg)

if 0 <= avg <= 39:
    print("D")
elif 40 <= avg <= 59:
    print("C")

elif 60 <= avg <= 79:
    print("B")

elif 80 <= avg <= 100:
    print("A")

else:
    print("Invalid")