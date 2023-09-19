#This is probably extremely excessive and redundant code but I really tried
#Zianab
#Aida
#Sofia
num_list=[0,0,0,0,0]
row=int(input("Enter a row num from 1 to 5: "))
col=int(input("Enter a col num from 1 to 5: "))
list_1=[]
if row>=1 and row<=5:
    if col>=1 and col<=5:
        if row==1:
            if col==1:
                num_list[0]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[0]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
            elif col==2:
                num_list[1]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[1]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
            elif col==3:
                num_list[2]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[2]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
            elif col==4:
                num_list[3]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[3]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
            else:
                num_list[4]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[4]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
        elif row==2:
            if col==1:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[0]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[0]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
            elif col==2:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[1]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[1]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
            elif col==3:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[2]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[2]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
            elif col==4:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[3]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[3]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
            else:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[4]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[4]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
        elif row==3:
            if col==1:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
                num_list[0]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[0]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
            elif col==2:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
                num_list[1]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[1]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
            elif col==3:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
                num_list[2]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[2]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
            elif col==4:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
                num_list[3]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[3]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
            else:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
                num_list[4]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[4]=0
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                print(nums)
        elif row==4:
            if col==1:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
                 num_list[0]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[0]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
            elif col==2:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
                 num_list[1]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[1]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
            elif col==3:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
                 num_list[2]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[2]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
            elif col==4:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
                 num_list[3]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[3]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
            else:
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 count=1
                 while count<4:
                     print(nums)
                     count+=1
                 num_list[4]=1
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
                 num_list[4]=0
                 nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                 print(nums)
        else:
            if col==1:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
                num_list[0]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[0]=0
            elif col==2:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
                num_list[1]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[1]=0
            elif col==3:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
                num_list[2]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[2]=0
            elif col==4:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
                num_list[3]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[3]=0
            else:
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                count=1
                while count<5:
                    print(nums)
                    count+=1
                num_list[4]=1
                nums= str(num_list[0])+" "+str(num_list[1])+" "+str(num_list[2])+" "+str(num_list[3])+" "+str(num_list[4])
                print(nums)
                num_list[4]=0
    else:
        print("Invalid input")
else:
    print("Invalid input")