name = " "
roll = None
mobile = None
course = " "


detail = {}


while True:
    print("_" * 30)
    print("1. Add student Details!")
    print("2. Remove student Details !")
    print("3. View Student Details!")
    print("4. Check Student Detail By Roll No!")
    print("5. Exit!")

    choice = int(input("Enter Your Choice: "))
    print("_" * 30)
    match choice:
        case 1:
            print("You Selected : Add student Details!")
            name = input("Enter Name: ")
            roll = int(input("Enter Roll No: "))
            mobile = int(input("Enter Mobile Number: "))
            course = input("Enter Course: ")
            print("Added Successfully!")

            detail[roll] = {
                "Name": name,
                "Roll": roll,
                "Mobile": mobile,
                "Course": course,
            }

            print("_" * 30)

            print(detail)

            print("_" * 30)

            print("Do You Add More Data? ")
            required = input("Yes/No : ").title()

            if required == "Yes":
                continue

        case 2:
            print("You Selected : Remove student Details !")
            check = int(input("Enter Student Roll No: "))

            if check in detail:
                detail.pop(roll)
                print("Removed Successfully!")
            else:
                print("Invalid Roll No!")

            print("_" * 30)
            print("Do You Remove More Student?")
            check = input("Yes/No: ").title()

            if check == "Yes":
                continue

        case 3:
            print("You Selected : View Student Details !")
            print("Student Details!")
            print(detail)

            print("_" * 30)
            print("Do You Remove More Student?")
            check = input("Yes/No: ").title()

            if check == "Yes":
                continue

        case 4:
            print("You Selected : Check Student Detail By Roll No!")
            print("Check Student Detail!")
            check = int(input("Enter Student Roll No: "))

            if check in detail:
                print("===Details===")
                print(detail[roll])
            else:
                print("Invalid Roll No")

            print("_" * 30)
            print("Do You Remove More Student?")
            check = input("Yes/No: ").title()

            if check == "Yes":
                continue

        case 5:
            print("You Selected : Exit !")
            print("Exit Successfully! ")
            break

        case _:
            print("Invalid Choice!")
