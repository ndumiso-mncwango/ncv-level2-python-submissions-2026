n = int(input("Enter a positive integer: "))
x = 1
sum = 0
for x in range(1,n+1):
    cube = x ** 3
    sum = sum + cube
    print(cube, end = " ")
    
print(sum)