
y=int(input("Enter the final year"))
print("The leap years are:")
for i in range(2021,y+1):
    if i%4==0:
       print(i)