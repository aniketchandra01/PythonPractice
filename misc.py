num = int(input("Enter the no. of elements : "))
list = []
for x in range(0,num):
    list.append(int(input("Enter the Element :")))
temp = []
count = 0
for x in list:
    for y in list:
        if x == y and x not in temp:
            count += 1


    if x not in temp:
        print(f"{x} - {count} times")
    temp.append(x)
    count = 0