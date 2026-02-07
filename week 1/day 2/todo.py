todo_list=[]
print("===TODO LIST APP ===")

while True:
    print("MENU")
    print("1.ADD TASK: ")
    print("2.VIEW TASKS: ")
    print("3.REMOVE TASKS: ")
    print("4.EXIT: ")

    choice=input("\nENTER CHOICE(1-4): ")

    if choice==1:
        task=input("ENTER TASK TO BE ADDED: ")
        todo_list.append(task)
        print("TASK ADDED")
    elif choice==2:
        if len(todo_list)==0:
            print("NO TASKS YET ")
        else:
            print("YOUR TASKS")
            for i in range(len(todo_list)):
                print(str(i+1)+".",todo_list[i])
    elif choice==3:
        if len(todo_list)==0:
            print("NO TO TASKS TO REMOVE")
        else:
            print("YOUR TAKS")
            for i in range(len(todo_list)):
                print(str(i+1)+".",todo_list[i])
            num=int(input("ENTER TASK NUMBER TO REMOVE: "))
            if    