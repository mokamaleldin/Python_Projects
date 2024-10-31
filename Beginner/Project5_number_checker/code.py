def user_choice():
    choice = "WRONG"
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")
                within_range = False
        else:
            print("Sorry that is not a digit!")

    print(choice)

user_choice()