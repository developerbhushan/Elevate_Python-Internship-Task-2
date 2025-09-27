# To DO Console Based APP

# Step 1 : Load Tasks from a file if it exits

try:
    with open("tasks.txt","r") as file :           # Open the file in read mode
        tasks = [line.strip() for line in file.readline()]         # Read each line and remove extra spaces/newlines
    
except FileNotFoundError:        # if the file doesn't exist yet
    tasks = []                 # Start with an empty list


# Step 2: Define a function to show taksk

def view_tasks():
    if not tasks:
        print("Not tasks found")   # If the line is empty

    else:
        print("\n Yours Tasks:")
        for idx,task in enumerate(tasks, 1):       # Show task with numbers
            print(f"{idx} : {task}")
    print()


# Step 3: Define a function to add task

def add_task():
    task = input("Enter Your Task: ")
    tasks.append(task)
    print(f"Task {task} Added successfully!\n")

# Step 4: Define a function to remove a task

def remove_task():
    view_tasks()         # Show tasks first
    if tasks:
        try:
            task_num = int(input("Enter task number want to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)           # Remove task from list
                print(f"Task {removed} Removed Successfuly..")
            else:
                print("Invalid Task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

# Step 5 :Save tasks to file

def save_tasks():
    with open("tasks.txt", "w") as file:       # Open file in write mode
        for task in tasks:
            file.write(task + "\n")            # Write each task in a new line


# Step 6: Main Program Loop

while True:
    print("=== To Do LIST MENU===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        view_tasks()
    
    elif choice == '2':
        add_task()
        save_tasks()   

    elif choice == '3':
        remove_task()
        save_tasks()   #Save Task After Removing

    elif choice == '4':
        save_tasks()       # Save before exit 
        print("Good Bye!!")
        break
    else:
        print("Invalid Choice. Please Try Again..\n")

            