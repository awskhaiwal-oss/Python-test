task_detail = {}
print("""=== To-Do List===
    1. Add Task
    2. Show Tasks
    3. Mark task as Done
    4. Exit""")
while True:
    user_operator = int(input("Enter your choice: "))
    match user_operator:
        case 1:
            task = input("Type your task name  which you want to add in To-Do List: ")
            task_detail[task] = "Not Done"
        case 2:
            print(task_detail)
        case 3:
            task = input("Please enter your task name which you want to mark as complete: ")
            task_detail[task] = "Done"
        case 4:
            break
        case _:
            print("Number is not valid")