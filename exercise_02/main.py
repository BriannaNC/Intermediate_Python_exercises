
import timeit as t
def fib(number:int):
    
    seq=[0,1]
    for i in range(2,number+1):
        next_term=seq[i-2]+seq[i-1]
        seq.append(next_term)
    print(seq[number])
    

user_input= int(input("Enter a number 15-35: "))
if user_input < 15 or user_input>35:
    print("Invalid number")
else:
    fib(user_input)
    #I googled the how to find the time a process took to run and it gave me the timeit() function
    sec= t.timeit()
    print("fib(",user_input,") took", sec, "seconds")

