## Daily_Planner_app_v2

import random
import os
import time
import datetime
import sys

tasks=[]
todays_date=datetime.date.today()
tasks_timestamps=[]

## lets get the staff details
## These details will be used all through the program 

staff_name=input("Enter your name: ")
staff_dept=input("Enter the department you work in: ")
staff_time=input('What is the time as at now! : ')

print('\n')
print("\033[1mHello {}\033[0m, of \033[1m{}\033[0m department. Lets help you plan your day".format(staff_name.title(), staff_dept.title()))
print('\n')
print("Today you begin at \033[1m{}\033[0m:hrs ".format(staff_time))
print("Ensure you work hard, have fun and make history!!!")
print('\n')
    
def add_task_staff():
    print('\n')
    print("\033[1m\033[42mHello Proceed to add your tasks: \033[0m")
    print('\n')
    print("Type exit to return to start menu")
    print('\n')
    
    ## Lets Make this repeat till the user cancels it 
    while True:  
        
        ## Initiate New task
        new_task=input("Add a new task: ")
        
        if new_task.lower()=="exit":
            print('\n')
            print("We will return to main menu in 5 seconds")
            countdown_indicator()
            print('\n')
            pick_options()
            
        else:        
            task_time_input=(input("Enter a time for your task: "))
            while task_time_input.isalpha():
                print("\033[1m\033[41mError!!: Time can only be numeric data \033[0m")
                print('\n')
                task_time_input=(input("Enter a time for your task: "))

            tasks.append(new_task)
            tasks_timestamps.append(task_time_input)
            print("\033[1m{}\033[0m has been added and should be carried out by \033[1m{}\033[0m hrs".format(new_task,task_time_input))
            print('\n')
            time.sleep(0.25)
        
        
    
def remove_task_staff():
    print('\n')
    print('\033[1m\033[46mSelect the task you want to remove\033[0m')
    print(' '*15, "or")
    print("Type exit to return to start menu")
    print('\n')
    
    
    while True:
        count=0
        ## Lets us print all the available tasks
        for task in tasks:
            count+=1
            print("{}.{}".format(count,task))
            
        ## Let us setup the conditionals to remove task
        print('\n')
        to_be_removed=input("Enter the task number you want removed: ")
        
        
        if to_be_removed.lower()=="exit":
            print('We will return you to main menu in 5 seconds!!')
            countdown_indicator()
            pick_options()
        
        ## lets now remove the items
        to_be_removed_index=int(to_be_removed)
            
        ## Let us remove some tasks
        print('\n')
        
        ##item_position=tasks.index(to_be_removed)
        ## Let us try to implement a try-except block to prevent this from throwing an error
        
        try:    
            removed_task=tasks.pop(to_be_removed_index-1)
        except IndexError:
            time.sleep(0.5)
            print("\033[0m\033[41mERROR!!.....No such task in the list\033[0m")
            print('\n')
            
        else:        
            print("\033[1m{}\033[0m has been removed".format(removed_task))
            time.sleep(0.25)
            print('\n')
        
    
    
def edit_task_staff():
    ## We will try to make edits to any additions that has been done
    print('\n')
    print('\033[1m\033[45mWhich task do you want to make changes to: \033[0m')
    print(' '*20, "or")
    print("Type exit to return to start menu")
    print('\n')
    
    ## We will keep the program running till the user specifies otherwise
    
    while True:
        
        count=0
        
    
        for task in tasks:
            count+=1
            print("{}.{}".format(count,task)) 
            
        ## Let us initiate the change 
        print('\n')
        to_be_replaced=input("select a task to be modified: ")
        
        if to_be_replaced.lower()=="exit":
            print("We will return you to the main menu in 5 seconds")
            countdown_indicator()
            pick_options()
        
    
        to_be_replaced_index=int(to_be_replaced)
        
        ##item_position=tasks.index(to_be_replaced)
        
        print('\n')
        
        ## Now we get the index and change the task 
        replacement_value=input("Enter your new task ")
        
        try:
            old_value=tasks[to_be_replaced_index-1]
            tasks[to_be_replaced_index-1]=replacement_value
        except:
            time.sleep(0.5)
            print('\033[1m\033[41mERROR..!!   No such task exists\033[0m')
            print('\n')
        else:
            print('\n')
            print("\033[1m{}\033[0m has been replaced with \033[1m{}\033[0m".format(old_value, replacement_value))
            time.sleep(0.25)
            print('\n')
        
    

def view_task_staff():
    ## We will now display all the tasks the staff inputed
    
    print('\n')
    print("\033[1m\033[42mHere is a list of all your tasks sceduled for \033[1m{}\033[0m".format(todays_date))
    print('\n')
    
    
    for task,tasks_time in zip(tasks,tasks_timestamps):
        task_num=tasks.index(task)
        print("{}. {} is to be performed at {} hrs".format(task_num+1, task,tasks_time))
    
    print("\n")
    
    exit_view=input("You can type exit to return to the main menu: ")
    if exit_view.lower()=="exit":
        print("We will return you to the main menu in 5 seconds")
        countdown_indicator()
        pick_options()
    
    
        
def exit_task_staff():
    ## We will use this function to exit the program
    print('\n')
    print("Thanks for your time, Apllication will close in 5 seconds ")
    countdown_indicator()
    print("\n")
    sys.exit()
    


def countdown_indicator():
    n=0
    while n<=4:
        print("\033[1m.\033[0m", end=" ")
        time.sleep(0.5)
        n+=1 
    
    
   
    
## Here we have initiated our four functionalities
## We shall pause for tonigt and then conpound eeverything tomorrow morning
## Cheers amigos

## Welcome to a new day, Now we strive to complete the cooking

def welcome_greeting():
    welcome_greetings="DAILY_PLANNER  📝📝"
    print("\033[1m \033[40m{: ^200}\033[0m" .format(welcome_greetings))
    
    
def pick_options():
    print('\n')
    print("Pls select an option by entering the event number: ")
    print("\n")
    
    ## Lets put all the available options in a dictionary
    
    options={1:"Add New Task", 2:"Remove a Task", 3:"Edit a Task", 4:"View Tasks", 5:"Exit Daily Planner"}
    
    ## Lets make a list of all the keys
    list_of_options_keys=list(options.keys())
    
    ## Now let us print out all the optons
    ## We might get fancy 
    
    for id,option in options.items():
        print("{}. {}".format(id, option))
        
    print('\n')
    
    
    ## lets print out the list of possible options n
    try:
        
        options_pick=input("Select the event number: ")
        options_pick1=int(options_pick)
        print('\n')
    except ValueError:
        print('\n')
        print('\033[31m\033[1mERROR!!.. Enter the number to select a menu item\033[0m')
        pick_options()
        
    else:
        
    
    
    ## At this stage we define what happens when each option is selected
    
    
        if options_pick1==list_of_options_keys[0]:    
            ## Call the add_task function
            add_task_staff()
            
        elif options_pick1==list_of_options_keys[1]:
            ## call the remove task function
            remove_task_staff()
            
        elif options_pick1==list_of_options_keys[2]:
            ## Call the edit task function
            edit_task_staff()
            
        elif options_pick1==list_of_options_keys[3]:
            ## Call the view tsk function
            view_task_staff()
            
        elif options_pick1==list_of_options_keys[4]:
            ## call the exit daily planner function
            exit_task_staff()
            
        else:
            print("\033[1m\033[41m ERROR!!: You have made an invalid selection \033[0m")
            print('\n')
            pick_options()
        
        
welcome_greeting()
pick_options()


## def add_task_timestamp():
    