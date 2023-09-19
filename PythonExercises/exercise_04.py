#Aida
#Sofia
#Zainab
n = int(input("Enter a number: "))
numList=[]
for x in range(n):
    print("Enter number",x+1,": ")
    number = float(input(""))
    numList.append(number)
avg = sum(numList)/n

print("List: ", numList)
print("Average: ",avg)