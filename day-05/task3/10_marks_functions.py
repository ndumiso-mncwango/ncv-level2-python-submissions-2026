#Ndumiso Mncwango 23 October 2026 Soshanguve
count = 0
i = 0
sum = 0
average = 0

def getMarks():
    count = 0
    i = 0
    marks = []
    mark = int(input("Enter mark: "))
    
    while mark != -1:
        marks.append(mark)
        i = i + 1
        mark = int(input("Enter mark: "))
        count += 1
    
    return marks

def print_list_size(marks):
    print(f"Our list has {len(marks)} elements")
    
def print_marks(marks):
    for x in range(len(marks)):
        print(marks[x])
def get_sum_of_marks(marks):
    sum = 0
    for i in range(len(marks)):
        mark = mark[i]
        sum = sum + mark
        return sum
def get_avg(marks):
    average = sum/len(marks)
    return avearge
def determine_highest(marks):
    highest = 0
    for i in range(len(marks)):
        current_mark = marks[i]
        if current_mark > highest:
            highest = current_mark
    print(f"The highest mark is {highest}")

menu = "Press 1: Capturing marks\n"
menu += "Press 2: Check number of marks\n"
menu += "Press 3: Calculate sum of marks\n"
menu += "Press 4: Find highest mark marks\n"
menu += "Press 5: exit\n"

print(menu)
choice = int(input("Choose from the menu: "))
entered_marks = []
while choice != 5:
    if choice == 1:
        entered_marks = getMarks()
        print(entered_marks)
    elif choice == 2:
        print_list_size(entered_marks)
    elif choice == 3:
        calc_sum = get_sum_of_marks(entered_marks)
        print(f"Sum = {calc_sum}")
    elif choice == 4:
        determine_highest(entered_marks)
    elif choice == 5:
        print("Thank you for using the application")
    else: print("Not in the menu")
    
    print(menu)
    choice = int(input("Choose from the menu: "))