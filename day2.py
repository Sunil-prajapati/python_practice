num = -50 
if num > 0:
    print("postive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
#Loop
fruits = ["Apple","banana","cherry"]
for fruit in fruits:
    print(fruit)
    
#Loop with range
for i in range(5):
    print(i)
    
    
#while
count = 5
while count > 0:
    #print(count)
    count -= 1
    
    
for i in range(10):
    if i == 5:
        break
    #print(i,"break")
    
    
#continue to skip that condition
for i in range(10):
    if i == 5:
        continue
    #print(i,"continue")
    
for i in range(10):
    if i % 2 == 0:
        continue
   # print(i)

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} not Prime")
            break
    else:
        print(f"{num} Prime")
else:
    print(f"{num} not Prime") 
            