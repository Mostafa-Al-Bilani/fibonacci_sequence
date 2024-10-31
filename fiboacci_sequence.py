number = int(input("Enter a number: "))
num1 = 0
num2 = 1 

for i in range(0, number+1):#we loop through the numbers
    if i == 0: # specail case
        print(0, end = " ")
    elif i == 1: #specail case
        print(1, end = " ")
    else:
        answer = num2 + num1 #we update the answer
        print(answer, end = " ") 
        num1 = num2 # updating num1 to the previous value of num2
        num2 = answer # updating num2 to the previous value of answer
        

        
             


