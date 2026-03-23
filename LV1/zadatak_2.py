
try:
    grade = float(input("Enter a grade between 0.0 and 1.0: "))
    if(grade < 0.0 or grade > 1.0):
        raise Exception("Number out of range.")

except NameError:
    print("You have to enter a number.")

except ValueError:
    print("You have to enter a number.")




else:
    if(grade >= 0.9):
        print("A")
    elif(grade >= 0.8):
        print("B")
    elif(grade >= 0.7):
        print("C")
    elif(grade >= 0.6):
        print("D")
    else:
        print("F")
