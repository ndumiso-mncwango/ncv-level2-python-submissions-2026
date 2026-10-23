mark = int(input("Enter a mark: "))
result = "null"
if mark >= 0 and mark <=100:
    if mark < 50:
        result = "Fail"
    else:
        if mark >= 50 and mark < 75:
            result = "Pass"
        else:
            result = "Distinction"
else:
    print("Enter a valid mark")
print(f"The result is: {result}")