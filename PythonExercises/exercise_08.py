#Sofia
#Zainab
#Aida
nums=[]
num_1=int(input("Enter number 1: "))
nums.append(num_1)
num_2=int(input("Enter number 2: "))
nums.append(num_2)
num_3=int(input("Enter number 3: "))
nums.append(num_3)
num_4=int(input("Enter number 4: "))
nums.append(num_4)
num_5=int(input("Enter number 5: "))
nums.append(num_5)
num_6=int(input("Enter number 6: "))
nums.append(num_6)
num_7=int(input("Enter number 7: "))
nums.append(num_7)
num_8=int(input("Enter number 8: "))
nums.append(num_8)
num_9=int(input("Enter number 9: "))
nums.append(num_9)
num_10=int(input("Enter number 10: "))
nums.append(num_10)

only_once=[]
for x in nums:
    x-=1
    count=nums.count(nums[x])
    if count==1:
        only_once.append(nums[x])
    
print("Original List: ",nums)
print("Num that appear once: ",only_once)

