#Ndumiso Mncwango 23 October 2026 Soshanguve
marks = []
mark = int(input("Enter mark: "))
count = 0
i = 0
sum = 0
average = 0
#store marks in the list
while mark != -1:
    marks.append(mark)
    i = i + 1
    mark = int(input("Enter mark: "))
    count += 1
#print the marks stored in the list
for i in range(0, count):
    print(marks[i])

#calculate the sum of the marks
for i in range(0, count):
    mark = marks[i]
    sum += mark

#Calculate the average
average = sum/count

#prints the sum of the marks
print(f"The sum of the marks is: {sum}")
#prints the average
print(f"The average of the marks is: {average:.2f}")