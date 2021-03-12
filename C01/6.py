
names = []
num = input("Enter Number : ")
a_count = 0

for i in range(int(num)):
    name = input("Enter name : ")
    names.append(name)

for name in names:
    count = name.count("a")
    a_count+=count

print(a_count)


