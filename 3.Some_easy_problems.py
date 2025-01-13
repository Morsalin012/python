# problem-1: Rectangle or Square check
a= int(input("Enter the length: "))
b= int(input("Enter the breadth: "))

if (a==b):
    print("It's a square")
else:
    print("It's a rectangle")


# problem-2: Find the largest numbr
a= int(input("Enter the value of a: "))
b= int(input("Enter the value of b: "))
c= int(input("Enter the value of c: "))

if (a>b and a>c):
    print("Largest number is a= ", a)
elif(b>a and b>c):
    print("Largest number is b= ", b)
else:
    print("Largest number is c= ", c)


# problem-3: Odd Even
num= int(input("Enter any number: "))
if (num%2==0):
    print("It's an Even number")
else:
    print("It's a odd number")


# problem-4: Marks
studentMarks = int(input())
if studentMarks > 90:
     print(studentMarks, ": Grade A")
elif studentMarks > 80 and studentMarks <= 90:
     print(studentMarks, ": Grade b")
elif studentMarks >= 60 and studentMarks <= 80:
     print(studentMarks, ": Grade c")
else:
     print(studentMarks, ": Grade d")


#problem-5: Leap year
inputYear = int(input("input year: "))
if inputYear % 100 == 0 and inputYear % 400 == 0:
    print(inputYear, ": it is leap year")
elif inputYear % 4 == 0 and inputYear % 100 != 0:
    print(inputYear, ": it is leap year")
else:
    print(inputYear, "it is not leap year")
