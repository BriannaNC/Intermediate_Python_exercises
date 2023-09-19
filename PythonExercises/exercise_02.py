#Aida
#Sofia
#Zainab
def suffix(str1,str2):
    return str1.endswith(str2) or str2.endswith(str1)

str1= input("Enter a string: ")
str2= input("Enter another string: ")
if suffix(str1,str2):
    print("True")
else:
    print("False")

    