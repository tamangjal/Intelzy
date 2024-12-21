def check_E_or_O(num):
    if num % 2==0:
        return "Even"
    else:
        return "odd"
#input the num from user
num=int(input("Enter the num:"))
result=check_E_or_O(num)
print(f"The number{num} is {result}.")