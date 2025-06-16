# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

# Task dictionary conatining the details of each task.
task_dict = {}
count = 1
with open("tasks.txt", "r") as t_file:
    tasks = t_file.readlines()

    for task in tasks:
        new_task = task.strip("\n")
        t = new_task.split(", ")
        task_dict[count] = t
        count += 1
        
            
def reg_user():
    
    '''This function takes input from the admin user to register a new user.
    It will request the new username and new password of the user to be 
    registered. The username will be appended to the username list and 
    password will be appended to the password list. The new user will 
    then be written to the text file "user.txt".
    '''
    
    new_username = input("New username: ")
    while True:
        new_username not in username
        if new_username in username:
            print("Username already taken. Please try a differnt username.\n")
            new_username = input("New username: ")
            # If username is already in username list, user prompted to try a
            # new username.
    
        # Username appended to end of username list.
        elif new_username not in username:
            username.append(new_username)
            
            new_password = input("New password: ")
            confirm_password = input("Confirm password: ")
            
            # If passwords don't match error message shown.
            if new_password != confirm_password:
                print("Passwords do not match\n")
                confirm_password = input("Confirm password: ")

            # If passwords match user is added.    
            if new_password == confirm_password:
                password.append(new_password)
                print("New user added")
                break

    # New username and password written to user.txt  
    with open("user.txt", "a") as user_file:
            user_file.write(f"\n{new_username};{new_password}")
                

def add_task():
        
        '''This function will allow a user to add a new task. It will ask
        for the user the task is assigned to, the task title, description 
        and due date. The task details will then be written to the text 
        file "tasks.txt".
        '''
        
        task_username = input("Name of user assigned to this task: ")
        
        while True:
            task_username in username
            if task_username not in username:
               print("User does not exist. Please enter valid username.\n") 
               
               task_username = input("Name of user assigned to this task: ")
               # If username entered is not in username, error message.

            elif task_username in username:
                task_title = input("Title of the task: ")
        
                task_description = input("Description of the task: ")
        
                curr_date = date.today()
        
                task_due_date = input("Due date of task YYYY/MM/DD: ")
        
                completed = "No"
                   
                # New task written to tasks.txt
                with open("tasks.txt", "a") as task_file:
                    task_file.write(f'''{task_username}, {task_title}, \
{task_description}, {task_due_date}, {curr_date}, {completed}\n''')
        
                print("Task successfully added.")
                break

        
def view_all():

    '''This function will allow a user to view all tasks assigned on 
    task_manager.py and will display them in a user-friendly manner.
    '''
    
    # Count to keep track of the number of tasks.
    task_count = 0

    for key in task_dict:
            task_count += 1
        
            # Displayed in user friendly format.
            print(
f'''---------------------------------------------------------------------

Task number:            {task_count}
Task:                   {task_dict[key][1]}
Assigned to:            {task_dict[key][0]}
Date assigned:          {task_dict[key][4]}
Due date:               {task_dict[key][3]}
Task completed?:        {task_dict[key][5]}
Task description:\n{task_dict[key][2]}

---------------------------------------------------------------------
''')


def view_mine():

    '''This function will allow a user to view all tasks assigned to them
    by reading from the text file "tasks.txt". The user then has the option
    to mark the task as complete or edit the task (given it is not already
    complete) by either changing the due date or changing the user the task 
    is assigned to.
    '''
    
    with open("tasks.txt", "r") as f:
        data = f.readlines()

        for pos, task in enumerate(data):
            split_data = task.split(", ")
            if curr_user == split_data[0]:
                print(
f'''---------------------------------------------------------------------

Task number:            {pos+1}
Task:                   {split_data[1]}
Assigned to:            {split_data[0]}
Date assigned:          {split_data[4]}
Due date:               {split_data[3]}
Task completed?:        {split_data[5]}
Task description:\n{split_data[2]}

---------------------------------------------------------------------
\n''')
                   
    while True:

        # Prompts user to select the task they wish to edit.
        select_task = int(input('''Enter the number of the task you wish to
select or enter -1 to return to the main menu: '''))
        edit_task = select_task - 1
    
        # If number entered is -1, return to main menu.
        if select_task == -1:
            print(menu)
            break
                
        # If number entered is higher than the length of data, error message.
        elif edit_task > len(data):
            print("Invalid number.\n")
    
            
        elif 0 <= edit_task < len(data):
            edit_data = data[edit_task]

            # User given options on how they would like to edit the task.
            chosen_option = input('''Select one of the following options:
c - Mark task as complete
e - Edit chosen task (only if task is not complete)
: ''').lower()
            
            # If task is already complete, user is informed.
            if chosen_option == "e":
                split_data = edit_data.split(", ")
                if split_data[5] in ["Yes", "Yes\n"]:
                    print(f'''Cannot edit as task has already  
been marked as complete.\n''')
                    break

                # If task is not complete, user is given options for editing.
                else:
                    choice = input('''\nSelect one of the following options:
u - Change the user the task is assigned to
d - Change the due date of the task
: ''').lower()
                    if choice == "u":
                        
                        change_user = input('''Enter the user you would
like to reassign this task to: \n''')
                        
                        if change_user not in username:
                            print("Invalid user.\n")
                           
                            change_user = input('''Enter the user you would
like to reassign this task to: \n''')
                        
                        # task_dict updated.
                        task_dict[select_task][0] = change_user
                        
                        # tasks.txt file updated.
                        split_data = edit_data.split(", ")
                        split_data[0] = change_user

                        new_data = ", ".join(split_data)
                        data[edit_task] = new_data

                        with open("tasks.txt", "w") as task_file:
                                for task in data:
                                    task_file.write(task)

                                print("New user asssigned.\n")
                                break

                    elif choice == "d":
                        change_due_date = input('''Enter the new due date of 
this task in the format: YYYY-MM-DD:\n''')
                        
                        # task_dict updated.
                        task_dict[select_task][3] = change_due_date

                        # tasks.txt file updated.
                        split_data = edit_data.split(", ")
                        split_data[3] = change_due_date

                        new_data = ", ".join(split_data)
                        data[edit_task] = new_data

                        with open("tasks.txt", "w") as task_file:
                                for task in data:
                                    task_file.write(task)

                        print("Due date for task changed.\n")
                        break
                       
            # Option to mark the task as complete.
            elif chosen_option == "c":
                task_dict[select_task][5] = "Yes"

                with open("tasks.txt", "r") as task_file:
                    edit_data = task_file.read()

                    split_data = edit_data.split(", ")
                    split_data[5] = "Yes\n"
                    new_data = ", ".join(split_data)
                    data[edit_task] = new_data
                    
                with open("tasks.txt", "w") as mark:
                    for task in data:
                        mark.write(task)

                print("Task marked as complete.\n")
                break   


def gen_rep():

    '''This function will generate two text files, "task_overview.txt" and 
    "user_overview.txt". The "task_overview.txt" file will contain statistics
    on the tasks in task_manager.py. The "user_overview.txt" file will contain
    statistics on the each users assigned tasks.
    '''

    curr_date = datetime.today()
    curr_date = datetime.strftime(curr_date,"%Y-%m-%d" )

    total_tasks = len(task_dict)
    total_users = len(username)

    # Variables for complete, incomplete and overdue tasks.
    complete_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    # Uses items from task_dict to check if tasks are complete,
    # incomplete or overdue.
    for key in task_dict:
        if task_dict[key][5] == "Yes":
            complete_tasks += 1

        if task_dict[key][5] == "No":
            incomplete_tasks += 1

        if task_dict[key][3] < curr_date:
            overdue_tasks += 1
            
        # Writes to task_overview.txt and displyed in a user friendly way.
        with open("task_overview.txt", "w") as t_ov_file:
            t_ov_file.write(
f'''---------------------------------------------------------------------
Task overview

Total number of tasks:            {total_tasks}
Completed tasks:                  {complete_tasks}
Uncompleted tasks:                {incomplete_tasks}
Overdue tasks:                    {overdue_tasks}
Incomplete task %:                {round((incomplete_tasks/len(task_dict)) * 100, 2)}%
Overdue task %:                   {round((overdue_tasks/len(task_dict)) * 100, 2)}%

---------------------------------------------------------------------
''')  

    # Empty string to store what is to be written to text file
    # "user_overview.txt".
    user_overview = "" 
    user_overview += f'''
---------------------------------------------------------------------
User overview

Total number of users:              {total_users}
Total number of tasks:              {total_tasks}
'''
        
    # Variables for the tasks, completed tasks, incomplete tasks
    # and overdue tasks of each user.
    for u in username:
        user_tasks = 0
        user_complete = 0
        user_incomplete = 0
        user_overdue = 0

        # Uses task_dict items to check tasks.
        for key in task_dict:
            if task_dict[key][0] == u:
                user_tasks += 1

            if task_dict[key][0] == u and task_dict[key][5] == 'Yes':
                user_complete += 1

            if task_dict[key][0] == u and task_dict[key][5] == 'No':
                user_incomplete += 1
             
            if task_dict[key][0] == u and task_dict[key][3] < curr_date:
                user_overdue += 1

        user_overview += f'''
Username:                           {u}
Number of tasks assigned to user:   {user_tasks}
% of tasks assigned to user:        {round((user_tasks/total_tasks) * 100, 2)}%
% completed tasks by user:          {round((user_complete/user_tasks) * 100, 2)}%
% incomplete tasks by user:         {round((user_incomplete/user_tasks) * 100, 2)}%
% overdue tasks by user:            {round((user_overdue/user_tasks) * 100, 2)}%
'''  
 
    # Written to user_overview.txt and displayed in a user-friendly way.
    with open("user_overview.txt", "w") as usr_ov_file:
        usr_ov_file. write(user_overview)

          
def stats():

    '''This function will display to the terminal the statistics written in
    the text files "task_overview.txt" and "user_overview.txt" in a 
    user-friendly manner.
    '''

    with open("task_overview.txt", "r") as t_ov_file:
        for stats in t_ov_file.readlines():
            print(stats)

    with open("user_overview.txt", "r") as usr_ov_file:
        for lines in usr_ov_file.readlines():
            print(lines)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.readlines()

# Dictionary containing the login credentials of users.
username_password = {}
username = []
password = []
for user in user_data:
    
    login = user.split(";")
    username.append(login[0])
    password.append(login[1].strip("\n")) 
    username_password["Usernames"] = username
    username_password["Passwords"] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    if curr_user not in username:
        print("User does not exist")

    else:
        curr_pass = input("Password: ")
        if curr_pass not in password:
            print("Incorrect password")

        else:
            print("Login successful")
            logged_in = True

while True:
    
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if curr_user == "admin":
        print()
        menu = input('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

        if menu == 'r':
            reg_user()

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()
            
        elif menu == 'vm':
            view_mine()

        elif menu == 'gr':
            gen_rep()
          
        elif menu == 'ds':
            # gen_rep() function called to create the text files 
            # "task_overview.txt" and "user_overview.txt" if they do 
            # not exist yet.
            gen_rep()
            stats()
           
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
           print("You have made a wrong choice, Please Try again")

    elif curr_user != "admin":
        print()
        menu = input('''Select one of the following options below:
a - Adding a task
va - View all tasks
vm - View my tasks
e - Exit
:''').lower()
        if menu == "a":
            add_task()

        elif menu == "va":
            view_all()

        elif menu == "vm":
            view_mine()

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
           print("You have made a wrong choice, Please Try again")

# I used https://github.com/BhavyaP17/Capstone-Project-III--Lists-Functions-and
# -String-Handling/blob/main/task_manager.py to help understand how to update
# text in a text file in my view mine function.