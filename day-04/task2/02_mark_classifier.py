mark = int(input("Enter a mark: "))
result = "null"
if mark >= 0 and mark <= 100:
    if mark >= 80:
        result= "Outstanding"
    elif mark >=70:
        result = "Highly Competent"
    elif mark >= 50:
        result= "Competent"
    elif mark >= 40:
        result= "Not yet competent"
    else:
        result = "Not Achieved"
else:
    print("invalid mark")
print(f"The result is: {result}")