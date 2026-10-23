#set up
import json
import os


#starter menu
mytasklist={}

#part for 1
def Add_task(mytasklist):
    name=input("Please enter the task's name:")
    description=input("Please enter description(optional):")
    #need to fill in later after i come up with a way to store description
    mytasklist[name]=[description,"Pending"]
    print(mytasklist)

#part for 2
def View_task(mytasklist):
    print(mytasklist)

#part for 3
def Edit_task(mytasklist):
    while True:
        
        name=input("Please enter the task's name that you want to edit:")
        if name in mytasklist:
            rename=input("Please enter the new name. If you don't want to change it, please enter 'no'")
            if rename=="no":
                rename=name
                pass
            else:
                mytasklist[rename]=mytasklist[name]
                mytasklist.pop(name)
            redescription=input("Please enter the new description. If you don't want to change it, please enter'no'")
            if redescription=="no":
                pass
            else:
                mytasklist[rename][0]=redescription
                #need to fill in later after i come up with a way to store description
            print(mytasklist)
            break
        else:
            print("Name Invalid.Please enter a valid name.")
            

#part for 4
def Delete_task(mytasklist):
    while True:
        name=input("Please enter the task you want to delete:")
        if name in mytasklist:
            mytasklist.pop(name)
            print(mytasklist)
            break
        else:
            print("Name Invalid. Please enter a valid name.")

#part for 5
def Mark_task(mytasklist):
    name=input("which task do you want to change:")
    if mytasklist[name][1]=="Pending":
        mytasklist[name][1]="Completed"
    else:
        mytasklist[name][1]="Pending"
    print(mytasklist)

#part for 6
def Filter_task(mytasklist):
    while True:
        filt=input("Which kind of tasks do you want to view, 'all','Completed' or 'Pending'?")
        if filt=="all":
            print(mytasklist)
            break
        elif filt=="Completed":
            for key,value in mytasklist.items():
                if value[1]=="Completed":
                    print(key,value)
            break
        elif filt=="Pending":
            for key,value in mytasklist.items():
                if value[1]=="Pending":
                    print(key,value)
            break
        else:
            print("Invalid input. Please enter 'all', 'Completed' or 'Pending'.")

#part for 7
def Load_task():
    #wait a sec im gonna search for it
    #define the same target folder and filename
    target_folder="output_data"
    file_path=os.path.join(target_folder,"mytasklist.json")
    #check if the file actually exists before trying to open it
    if os.path.exists(file_path):
        with open(file_path,"r") as json_file:
            mytasklist=json.load(json_file)
        print("File loaded successfully!")
        return mytasklist
    else:
        print(f"Error: Could not find the file at {file_path}")

#part for 8
def Save_task(mytasklist):
    #wait again
    #define the folder name you want to save in
    target_folder="output_data"
    #automatically create the folder if it doesn't exist
    os.makedirs(target_folder,exist_ok=True)
    #combine the folder path and the file name
    #using os.path.join handles slashes correctly on both Windows and Mac/Linux
    file_path=os.path.join(target_folder,"mytasklist.json")
    #save the dictionary as a json file
    with open(file_path,"w") as json_file:
        #indent=4 makes the file structured and easy to read
        json.dump(mytasklist, json_file,indent=4)
        print("Mytasklist successfully saved as 'mytasklist.json'!")
        print(f"File saved to subfolder:{file_path}")
        
        
while True:
    print("\nTo-Do List Application")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Edit Task")
    print("4.Delete Task")
    print("5.Mark Task as Completed or Pending")
    print("6.Filter Tasks")
    print("7.Load Tasks")
    print("8.Save Tasks")
    print("9.Exit")

    choice=int(input("Enter your choice:"))

    #TODO:Call appropriate function
    #TODO:handle invalid choices and exit when requested
    if choice==9:
        break  #exit
    elif choice==1:
        Add_task(mytasklist)
    elif choice==2:
        View_task(mytasklist)
    elif choice==3:
        Edit_task(mytasklist)
    elif choice==4:
        Delete_task(mytasklist)
    elif choice==5:
        Mark_task(mytasklist)
    elif choice==6:
        Filter_task(mytasklist)
    elif choice==7:
        mytasklist=Load_task()
        print(mytasklist)
    elif choice==8:
        Save_task(mytasklist)
    else:
        print("Your input is invalid, please input numbers between 1 ad 9")
        #handle invalid choices
