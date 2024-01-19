tasks=[]
def add_task(task):
    tasks.append(task)
    print(f'Task {task} added to the to do list ')
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'task {task} removed from the to do list')
    else:
        print(f"task {task} is not found in the to do list")
def display_task():
    if tasks:
        print('\n to-do list:')
        for index,task in enumerate(tasks,start=1):
            print(f'{index}.{task}')
        else:
            print('\n to-do list is empty')
while True:
    print('\n option')
    print('1.add a task')
    print('2.remove the task')
    print('3.display the task')
    print('4.exit')
    choice=int(input('enter your choice(1/2/3/4):'))
    if choice==1:
        task=input('enter the task to add:')
        add_task(task)
    elif choice==2:
        task=input('enter the task to remove: ')
        remove_task(task)
    elif choice==3:
        display_task()
    elif choice==4:
        print('exiting the to-do list')
        break
    else:
        print('invalid choice')                
                                     