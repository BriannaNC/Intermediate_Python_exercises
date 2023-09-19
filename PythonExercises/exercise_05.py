#Zainab
#Aida
#Sofia
nums_1=[]
nums_2=[]
count_1=0
count_2=0
while count_1<5:
    nums_1.append(int(input("Enter a number for the first list: ")))
    count_1+=1
while count_2<5:
    nums_2.append(int(input("Enter a number for the second list: ")))
    count_2+=1
nums_3=[]
for nums in nums_1:
    if nums in nums_2:
        nums_3.append(nums)
print("First List: ",nums_1)
print("Second List: ",nums_2)
print("Common List: ",nums_3)
