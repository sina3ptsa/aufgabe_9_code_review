import csv

# A class for tasks
class Task():
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        if priority == 1 or priority == "low":
            self.priority = "low"
        elif priority == 2 or priority == "med":
            self.priority = "med"
        elif priority == 3 or priority == "high":
            self.priority = "high"

# A class for the to do list we're gonna make
class ToDoList():

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_list(self):
        print(f"{'Number':<8} | {'Name':<20} | {'description':<30} | {'Priority':<10}")
        for number, task in enumerate(self.tasks, start = 1):
            print(f"{number:<8} | {task.name:<20} | {task.description:<30} | {task.priority:<10}")

    def load_csv(self):

        with open ('to_do_list.csv', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                task_n = Task(row["name"], row["description"], row["priority"])
                self.add_task(task_n)

    def save_list(self):
        with open ('to_do_list.csv', 'w', newline="") as csv_file:
            fieldnames = ['name', 'description', 'priority']
            writer = csv.DictWriter(csv_file, fieldnames= fieldnames)

            writer.writeheader()
            for row in self.tasks:
                writer.writerow({'name': row.name, 'description': row.description, 'priority': row.priority})

# The text interface
number = 0
to_do_list = ToDoList()
to_do_list.load_csv()

while number != 5:
    print(
        "Insert the command number\n" \
        "1. View tasks\n" \
        "2. New task\n" \
        "3. Delete task\n" \
        "4. Save list\n" \
        "5. Exit"
    )
    number = input()
    try:
        number = int(number)
        if number == 1:
            to_do_list.show_list()

        elif number == 2:
            name = input("Insert new task's name\n")

            description = input("Insert new task's description\n")
            while True:
                priority = input(
                    "Insert new task's priority number\n" \
                    "1. low\n" \
                    "2. mid\n" \
                    "3. high\n"
                )
                try:
                    priority = int(priority)
                    if priority in (1, 2, 3):
                        break
                except ValueError:
                    print("You can only insert one of the three numbers for priority!")
                    continue
                else:
                    print("You can only insert one of the three numbers for priority!")

            new_task = Task(name= name, description= description, priority= priority)
            to_do_list.add_task(new_task)

        elif number == 3:

            while True:
                to_do_list.show_list()
                number_3_1 = input("Insert the number of the task you want to delete\nInsert r for retuning to the main menu\n")
                if number_3_1 == "r":
                    break
                else:
                    try:
                        number_3_1 = int(number_3_1)
                    except ValueError:
                        print("Input is not valid.")
                        continue
                    
                    if number_3_1 in range(1, len((to_do_list.tasks))+1):
                        while True:
                            yes_or_no = input(f"Are you sure to delete task number {number_3_1}?\nInsert y for Yes.\nInsert n for No\n")
                            if yes_or_no == "y":
                                print(f"Task number {number_3_1}. {to_do_list.tasks[number_3_1-1].name} has been deleted.")
                                to_do_list.remove_task(to_do_list.tasks[number_3_1 - 1])
                                break
                            elif yes_or_no == "n":
                                break
                            else:
                                print("Input is not valid!")    
                    else:
                        print("Input is not valid!")
                        continue

        elif number == 4:
            to_do_list.save_list()
            print("Changes have been saved on the csv file.")
        elif number == 5:
            break
        else:
            print("You can only insert one of the command numbers!")
    except ValueError:
        print("You can only insert a command number!\n")    
