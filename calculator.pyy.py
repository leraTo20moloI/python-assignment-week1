def add(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
        return "Error ! division by zere!!"
    else:
        return x/y
    
    def calculator():
        print("welcome to python by zero")
        print("select an operator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("enter your choice (1/2/3/4/5) : ")
        
        if choice in ['1','2','3','4']:
            num1 =float(input("Enter the first number :"))
            num2 =float(input("Enter the second number :"))
            
            if choice =='1':
                print(f"the result is: {add(num1,num2)}")
            elif choice =='2':
                print(f"the result is: {subtraction(num1,num2)}")
            elif choice =='3':
                print(f"the result is: {multiply(num1,num2)}")
            elif choice =='4':
                print(f"the result is: {division(num1,num2)}")
            elif choice =='5':
                print("Exiting the calculator ..GoodBye!")
            else:
                print("Invalid selection please select a valid number")
                
            calculator()