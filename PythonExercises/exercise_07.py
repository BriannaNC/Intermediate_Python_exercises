#Aida
#Sofia
#Zainab
go=True
nums=[]
evens=[]

while go:
    inputs=input("Enter a number or QUIT to quit: ")
    if inputs == "QUIT":
        go=False
    else:
        inputs=int(inputs)
        nums.append(inputs)



print("All Nums: ",nums)
for x in nums:
    x-=1
    if nums[x]%2==0:
        evens.append(nums[x])
print("Even Nums: ", evens)
