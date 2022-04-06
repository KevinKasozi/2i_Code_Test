"""
Hello Team, 

Welcome to the Multiplication Program. Per the instructions below i have created the program

Task : In a language of your choice, using all best practice principles you’re aware of, could you please provide code that iterates in multiples of A until X, then in multiples of A + 1 until 2X, 
then multiples of A + 2 until 3X. Please state any assumptions you’ve made.

My assumptions regarding the task is that you wanted to provide a code that takes in a value called multiply which is an integer and a value that we want the program to be multplied by x amount of times.
The program will need to iterate through a

x = 10
A times 

"""

#creating a function that will calulate the equation specified for the task. It will take in the arguements which will be used as a range to iterate through and multiplied.
def multiplesofvalue (value_to_mutliply):

    # This outer loop will generate the rows for the program. The row program will use the values set in the list using range().The values set in the range below means the outer loop will iterate 3 times.
    for multiplier in range (1,4):
       
        for x in range (value_to_mutliply):   #this is a nested for loop. This for loop iteration will be dependant on the outer values of the outer loop. As this loop is dependant on the value of the outloop , this for loop will get that value and times it by the all the values found in the arguement value_to_mutliply, one after another
            x+=1       #count = count +1 in the value_to_mutliply arguement.
            print(x*multiplier,end=" ") #This will print the results of the for loop. 

        print() #This will add a new line after each iteration of my outerloop to display the numbers more clearly.
            
multiplesofvalue(10)  # Here we are calling the function multiplesofvalue and passing through the arugmenet for the function. The function should carry out the equation to meet the expectations of the arguemnt. 

