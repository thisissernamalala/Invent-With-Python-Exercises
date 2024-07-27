
count = 0
sum = 0.0
av = 0
print(type(int("55")))
while True:
    userIn = input("Enter a number: ")
    if userIn == "done":
        break
    try:
        fval = float(userIn)
    except:
        print("Invalid Input")
        continue
    count+=1
    sum+=fval
av = sum/count
print("ALL DONE!")
print(f"The sum: {sum}")
print(f"The count: {count}")
print(f"The average: {av}")
