age = int(input("Enter age: "))
job = input("Do you have a job? (y/N): ")
income = int(input("Enter monthly income: "))

if age >= 21 and age <= 65:
    if job == "y":
        if income >= 5000:
            print("Approved")
        elif income >= 3000:
            print("Approved with conditions")
        else:
            print("Rejected: low income")
    else:
        print("Rejected: no job")
else:
    print("Rejected: age not eligible")
