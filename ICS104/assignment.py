import pandas as pd
import os

# Read the Excel sheet by in putting file path
pathInput = input("Enter the path of the Excel sheet: ")

#check to see if other formats of files are uploaded
while (pathInput.endswith("xlsx") == False and pathInput.endswith("csv") == False):
    print("The file is not in xlsx or csv format")
    print("Please upload the file in xlsx or csv format")
    pathInput = input("Enter the path of the Excel sheet: ")

#check to see path exists or not
while (os.path.exists(pathInput) == False):
    print("The path does not exist")
    print("Please enter a valid path")
    pathInput = input("Enter the path of the Excel sheet: ")

#check if data exists in every coloumn and row
if pathInput.endswith("xlsx") == True:
    df = pd.read_excel(pathInput)
    while (df.isnull().values.any() == True):
        print("The data is not complete")
        print("Please upload the file with complete data")
        pathInput = input("Enter the path of the Excel sheet: ")
        df = pd.read_excel(pathInput)
else:
    df = pd.read_csv(pathInput)
    while (df.isnull().values.any() == True):
        print("The data is not complete")
        print("Please upload the file with complete data")
        pathInput = input("Enter the path of the Excel sheet: ")
        df = pd.read_csv(pathInput)


#Main function
def main():
    #print the main menu
    printMenu()
    #ask the user to enter a number
    choice = input("Enter a number: ")
    #check to see if the entered value is in integer format or not
    #input validation to make sure the user enters a number between 1 and 8
    while (choice.isdigit() == False or int(choice) < 1 or int(choice) > 8 ):
        print("Please enter a number between 1 and 8")
        choice = input("Enter a number: ")
    #call function based on the user's choice
    if choice == "1":
        findTask()
    elif choice == "2":
        addTask()
    elif choice == "3":
        modifyTask()
    elif choice == "4":
        removeTask()
    elif choice == "5":
        printEmployeeTasks()
    elif choice == "6":
        printPriorityTasks()
    elif choice == "7":
        saveFile()
    elif choice == "8":
        print("Thank you for using the program")
        exit()
        
#This function will print the main menu
def printMenu():
    print("1. Find a task by name")
    print("2. Add a new task")
    print("3. Modify the status of an existing task")
    print("4. Remove an existing Task")
    print("5. Print all the tasks that were assigned to a specific employee")
    print("6. Print all the tasks that have the priority x")
    print("7. Save the file in the same excel sheet")
    print("8. To close the program")

#This function will ask the user to enter a Task and then display the task details.
def findTask():
    #ask the user to enter a Task
    try:
        taskName = str(input("Enter the Task: ")).capitalize()
    except ValueError:  
        print("Please enter the Task name in string format")
    #search for the Task in the excel sheet
    task = df.loc[df['Tasks'] == taskName]
    #check to see if the task exists or not
    while (task.empty == True):
        print("The task does not exist")
        print("Please enter a valid task")
        taskName = str(input("Enter the Task: ")).capitalize()
        task = df.loc[df['Tasks'] == taskName]
    #get the data from each coloumn and print the task details 
    for index, row in task.iterrows():
        print("Task: ", row['Tasks'])
        print("Priority: ", row['Priority'])
        print("Assigned To: ", row['Assigned to'])
        print("Assign Date: ", row['Assigned'])
        print("Due Date: ", row['Due'])
        print("Status: ", row['Status'])
    #print(task)
    #ask the user if they want to continue
    continueProgram()

#This function will ask the user to enter the task details and then add the task to the list.
def addTask():
    #ask the user to enter the task details
    try:
        taskName = str(input("Enter the Task: ")).capitalize()
        taskPriority = str(input("Enter the task priority: ")).capitalize()
        taskAssignedTo = str(input("Enter the task assigned to: ")).capitalize()
        taskAssignDate = input("Enter the task assigned date (DD/MM/YYY): ")
        taskDueDate = input("Enter the task due date (DD/MM/YYY): ")
        taskStatus = "0%"
    except ValueError:
        print("Please enter the correct data type")
    #add the task to the list
    df.loc[len(df)] = [taskName, taskPriority, taskAssignedTo, taskAssignDate, taskDueDate, taskStatus]
    #remove timestamp from the date before saving the file
    df['Assigned'] = pd.to_datetime(df['Assigned']).dt.strftime('%d/%m/%Y')
    df['Due'] = pd.to_datetime(df['Due']).dt.strftime('%d/%m/%Y')
    print("Task added successfully")
    #save the file
    print("Please go back to main menu and save file before exiting the program")
    #ask the user if they want to continue
    continueProgram()

#This function will ask the user to enter a Task and then modify the status of the task to either “Not Started”, “In Progress” or “Completed”.
def modifyTask():
    #ask the user to enter a Task
    try:
        taskName = str(input("Enter the Task: ")).capitalize()
    except ValueError:  
        print("Please enter the Task name in string format")
    #search for the Task in the excel sheet
    task = df.loc[df['Tasks'] == taskName]
    #if the task does not exist then ask the user to enter a valid task
    while (task.empty == True):
        print("The task does not exist")
        print("Please enter a valid task")
        taskName = str(input("Enter the Task: "))
        task = df.loc[df['Tasks'] == taskName]
    #get data from each coloumns and print the task details
    for index, row in task.iterrows():
        print("Task: ", row['Tasks'])
        print("Priority: ", row['Priority'])
        print("Assigned To: ", row['Assigned to'])
        print("Assign Date: ", row['Assigned'])
        print("Due Date: ", row['Due'])
        print("Status: ", row['Status'])
    #save the status value of the task in a variable
    oldStatus = task['Status'].values[0]
    #ask the user to enter the new status
    newStatus = str(input("Enter the new status: "))
    #replace the old status with the new status
    df['Status'] = df['Status'].replace(oldStatus, newStatus)
    print("Status updated successfully")
    #save the file
    print("Please go back to main menu and save file before exiting the program")
    #ask the user if they want to continue
    continueProgram()

#This function will ask the user to enter a Task and then remove the task from the list.
def removeTask():
    #ask the user to enter a Task
    taskName = input("Enter the Task: ").capitalize()
    #check if the task exists
    if df.loc[df['Tasks'] == taskName].empty:
        print("Task does not exist")
    else:
        #search for the Task in the excel sheet
        task = df.loc[df['Tasks'] == taskName]
        #get data from each coloumn and display the task details
        for index, row in task.iterrows():
            print("Task: ", row['Tasks'])
            print("Priority: ", row['Priority'])
            print("Assigned To: ", row['Assigned to'])
            print("Assign Date: ", row['Assigned'])
            print("Due Date: ", row['Due'])
            print("Status: ", row['Status'])  
        #ask the user to confirm the removal
        confirm = input("Are you sure you want to remove this task? (Y/N): ").upper()
        #if the user confirms the removal
        if confirm == "Y":
            #remove the task from the list
            df.drop(df.loc[df['Tasks'] == taskName].index, inplace=True)
        #save the file
        print("Please go back to main menu and save file before exiting the program")
        #ask the user if they want to continue
        continueProgram()

#This function will ask the user to enter an employee name and then display all the tasks that were assigned to that employee.
def printEmployeeTasks():
    #ask the user to enter an employee name
    employeeName = input("Enter the employee name (Case sensitive!): ").capitalize()
    #search for the employee name in the excel sheet
    employee = df.loc[df['Assigned to'] == employeeName]
    #check if the employee exists
    while employee.empty:
        print("Employee does not exist")
        printEmployeeTasks()
    #get data from each coloumn and display the task details
    for index, row in employee.iterrows():
        print("Task: ", row['Tasks'])
        print("Priority: ", row['Priority'])
        print("Assigned To: ", row['Assigned to'])
        print("Assign Date: ", row['Assigned'])
        print("Due Date: ", row['Due'])
        print("Status: ", row['Status'])
        print("\n")
    #ask the user if they want to continue
    continueProgram()
    
#This function will ask the user to enter a priority level and then display all the tasks that have the priority x.
def printPriorityTasks():
    #ask the user to enter a priority level
    priorityLevel = input("Enter the priority level (High, Medium, Low): ").capitalize()
    #check if the priority level is valid, if invalid keep asking the user to enter a valid priority level
    if priorityLevel not in ("High", "Medium", "Low"):
        print("Invalid priority level")
        printPriorityTasks()
    else:
    #search for the priority level in the excel sheet
        priority = df.loc[df['Priority'] == priorityLevel]
        #get data fom coloumns and display the task details
        for index, row in priority.iterrows():
            print("Task: ", row['Tasks'])
            print("Priority: ", row['Priority'])
            print("Assigned To: ", row['Assigned to'])
            print("Assign Date: ", row['Assigned'])
            print("Due Date: ", row['Due'])
            print("Status: ", row['Status'])
            print("\n")
    #ask the user if they want to continue
    continueProgram()

#This function will save the file in the same excel sheet.
def saveFile():
    #check the file format
    if pathInput.endswith(".csv"):
        #save the file in the same excel sheet
        df.to_csv(pathInput, index=False)
    elif pathInput.endswith(".xlsx"):
        #save the file in the same excel sheet
        df.to_excel(pathInput, index=False)
    #ask the user if they want to continue
    closeProgram()

#This function will close the program.
def closeProgram():
    print("Program closed")
    exit()

#This function will ask the user if they want to continue
def continueProgram():
    cont = input("Do you want to continue? (Y/N): ").upper()
    if cont == ("Y"):
        main()
    else:
        print("Thank you for using the program")
        exit()

#Call the main function
main()
