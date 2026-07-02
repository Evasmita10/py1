print("--WELCOME to TO-DO-LIST")

tasks=[]

while True:
 print("1. Add Task")
 print("2. View Tasks")
 print("3. Remove Tasks")
 print("4. Exit")

 choice=input("Enter your choice: ")

 if choice=="1":
    task=input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

 elif choice=="2":
    if len(tasks)==0:
        print("No tasks available.")
    else:
        print("\n Your Tasks: ")
        for i in range(len(tasks)):
            print(i+1,".",tasks[i])

 elif choice=="3":
    if len(tasks)==0:
        print("No tasks to remove")
    else:
        print("\n Your Tasks: ")
        for i in range(len(tasks)):
            print(i+1,".",tasks[i])  

        num=int(input("Enter task to remove: "))
        if 1<=num<=len(tasks):
            removed_task=tasks.pop(num-1)
            print((f"Task '{removed_task}' removed")) 
        else: 
            print("Invalid task number!")

 elif choice=="4":
    print("Exiting to-o-list. GOODBYE!")
    break

else:
    print("Invalod chooce. Please enter 1-4: ")



