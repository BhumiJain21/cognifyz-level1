#LEVEL-01
# Task:1 -> String Traversal
def reversal(s):
    return s[::-1]
s=input("Enter String:")
print (reversal(s))

#Task:2 -> Temperature converter
temp=(input("Enter Temperature  with Degree  :"))
degree= int(temp[ : -1])
conv= temp[-1]
if conv.upper() =="C":
    result=int(round((9*degree)/5+32))
    convo="Fahrenheit"
elif conv.upper()=="F":
    result=int(round((degree-32)*5/9))
    convo="Celsius"
else:
    print("Input proper Degree")
    quit()
print("The temperature in" , convo, "is",  result,"degrees.")

#Task:3 -> Email Validator
import re
pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+$"
def email_validator(email):
    if (re.fullmatch(pattern,email)):
        print("Valid Email")
    else:
        print("Invalid Email")
email=input("Enter your Email:")
email_validator(email)

#Task: 4 -> Simple Calculator
num1=int(input("Enter First Operand:"))
num2=int(input("Enter Second  Operand:"))
print ("press 1:For ADD -- press 2: For Subtraction --press 3: For Multiply --press 4: For Division --press 6: For Percentage ")
op=int(input("Enter which Operation you want to perform :"))
if op==1:
    print("Addition of" , num1, "and", num2,"is",(num1+num2))
elif op==2:
    print("Subtraction of " , num1, "and", num2, "is" ,(num1-num2))
elif op==3:
    print("Multipication of" , num1, "and", num2,"is",(num1*num2))
elif op==4:
    print("Multipication of ", num1,"and",num2,"is ",(num1*num2))
elif op==5:
    if num2==0:
         print("invalid !!")
    else:
        print("Division of",num1,"and",num2,"is",(num1/num2))
elif op==6:
    print("Percentage of",num1,"and",num2,"is",(num1/num2)*100,"%")
else:
    print("invalid operation choosed")

#Task:5-> Palindrome Chcecker
def checker(s):
    if(s==s[::-1]):
        print("Yes, It is a Palindrome")
    else:
        print("No , it is not a Palindrome")
s=input("Enter a string to check whether it is palindrome or not :")
(checker(s))






