def total_euro(hours, wage):
    return hours*wage


hours = float(input("Enter working hours:"))
wage = float(input("Euro/h:"))

print(total_euro(hours, wage))

