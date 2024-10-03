students = []

while True:
    print('\n 1. Add a new student')
    print('\n 2. Show all students')
    print('\n 3. Exit')
    choice = input("Choose a number: ")

    if choice == "1":
        name = input("Enter the student's name: ")
        age = input("Enter the student's age: ")
        grade = input("Enter the student's grade: ")
        scores = []

        while True:
            subject = input("Enter the subject name: ")
            score = int(input(f"Enter the score for {subject}: "))
            scores.append(f'{subject}: {score}')

            # Add more subjects, yes or no
            more = input("Do you want to add more subjects (yes/no): ")
            if more != 'yes':
                break
        
        students.append({"name": name, "age": age, "grade": grade, "scores": scores})
        
    elif choice == "2":
        if len(students) == 0:
            print("We don't have any students yet.")
        else:
            for student in students:
                print(f"Name: {student['name']} - Age: {student['age']} - Grade: {student['grade']}")
                print("Score Results:")
                for score in student['scores']:
                    print(f'{score}')
                    
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("You entered an invalid number.")
