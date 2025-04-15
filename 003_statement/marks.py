marks = int(input("enter marks : "))

if marks>90 and marks<=100:
    print("A")
elif marks>70 and marks<=90:
    print("B")
elif marks>50 and marks<=70:
    print("C")
elif marks>35 and marks<=50:
    print("D")
elif marks>=0 and marks<=35:
    print("F")
else :
    print("Invalid input")