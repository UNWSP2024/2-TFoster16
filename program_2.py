#Timothy Foster, 1/28/25, Average Age Program

def average_age():
    # Get User Input.
    age1 = float(input("Enter the age of your first friend."))
    age2 = float(input("Enter the age of your second friend."))
    age3 = float(input("Enter the age of your third friend."))
    age4 = float(input("Enter the age of your fourth friend."))
    age5 = float(input("Enter the age of your fifth friend."))

    # Sum Ages.
    ageSum = age1 + age2 + age3 + age4 + age5

    # Average the ages.
    ageAverage = ageSum/5.0

    # Print the results.
    print("Your friends have an average age of", ageAverage, "years.")

# Line which calls the above function.
average_age()
