
numbers = []

while 1:
    user_input = input("Enter a number or 'Done' if you are finished: \n")
    if user_input.isdigit() == True :
        numbers.append(int(user_input))
    elif user_input == "Done":
        break
    elif user_input.isdigit() == False :
        print("Please enter a number or the word 'Done'.")
    
    

print("Number count: ", len(numbers))
print("Average: ", sum(numbers) / len(numbers))
print("Min Value: ", min(numbers))
print("Max Value: ", max(numbers))

numbers.sort

print(numbers)