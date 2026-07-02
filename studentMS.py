students={} 

print("🧑‍🎓 STUDENT RESULT MANAGEMENT SYSTEM🧑‍🎓")

while True:
    print("\nChoose an option: ")
    print("1. Add Student Result ")
    print("2. View Student Result")
    print("3. Exit ")

    choice=input("Enter your choice: ")

    if choice=="1":
        name=input("Enter student name: ").strip().title()
        math=int(input("Enter mathametics marks: "))
        mfcs=int(input("Enter MFCS marks: "))
        dbms=int(input("Enter DBMS name: "))
        aec=int(input("Enter AEC marks: "))
        py=int(input("Enter python marks: "))
        os=int(input("Enter operating system marks: "))

        total=math+mfcs+dbms+aec+py+os
        percentage=total/6

        if percentage>=90:
            grade="A+"
        elif percentage>=80:
            grade="A"
        elif percentage>=70:
            grade="B"
        elif percentage>=60:
            grade="C"
        elif percentage>=50:
            grade="D"
        else:
            grade="fail"   

        students[name]= {
            "Math":math,
            "MFCS":mfcs,
            "DBMS":dbms,
            "AEC":aec,
            "python":py,
            "operating system":os,
            "total":total,
            "Percentage":percentage,
            "Grade":grade 
        }

        print("✅Student result added successfully!")

    elif choice=="2":
        name=input("Enter student name to view result: ").strip().title()

        if name in students:
            print("\n📃 Student Result")
            print("Name: ",name)
            print("Math: ",students[name]["Math"])
            print("MFCS: ",students[name]["MFCS"])
            print("AEC: ",students[name]["AEC"])
            print("python: ",students[name]["PYTHON"])
            print("operating system:",students[name]["OS"])
            print("DBMS: ",students[name]["DBMS"]) 
            print("total: ",students[name]["DBMS"]) 
            print("percentage: ",students[name]["percentage"]) 
            print("Grade: ",students[name]["Grade"]) 
        else:
            print("❌ Student not found.")

    elif choice=="3":
        print("👏Exiting program Goodbye!")
        break

    else:
        print("❌Invalid choice. Please enter 1,2,or 3.")           




    
    