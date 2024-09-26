#Day2
name=input("Enter your name:")
print("Name:",name)
age=input("Enter your age:")
age=int(age)
print("Age",age)
if age<18:
    print("I don't have NID")
else:
    print("I have NID")
     #operator
female=False
male=False
""""
write a console program that takes number as input from user where number must be with in 0-100 and calculate division of user.
you are allowed to use 'input and print the fuction,if elif else'sytax
Division :
less than 40:fail
40-49:Third
50-59:Fecond
60-79:First
80-100:Distination
"""

marks=input("Enter your marks: ")
marks=int(marks)
print("Marks",marks)
if marks>=0 and marks <=100:
    if marks<40:
        print("Your are fail")
    elif marks>40 and marks<=49:
        print("you got third divison")
    elif marks>50 and marks <= 59:
      print("you got Secind divison") 
    elif marks>=60 and marks<=79:
        print("you got First divison")
    else:
        print("you got Distination")
else:
    print("Invalid inputs")

    
    #string interpollation
    name="Jal"
    age="24"
    sentance= f"Hi {name}! you are {age} years old."
    print(sentance)