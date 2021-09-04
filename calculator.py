name=input("Enter your name: ")
print("Welcome",name)
while True:
    print() 
    print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.FLOOR DIVISION\n6.EXIT ")
    operation=int(input("Enter the operation to perform: "))

    if operation ==1:
        no1=int(input("enter the number: "))
        no2=int(input("enter the number: "))
        print(no1,"+",no2,"=",no1+no2)

    elif operation ==2:
        no1=int(input("enter the number: "))
        no2=int(input("enter the number: "))
        print(no1,"-",no2,"=",no1-no2)

    elif operation ==3:
        no1=int(input("enter the number: "))
        no2=int(input("enter the number: "))
        print(no1,"x",no2,"=",no1*no2)

    elif operation ==4:
        no1=int(input("enter the number: "))
        no2=int(input("enter the number: "))
        print(no1,"/",no2,"=",no1/no2)

    elif operation ==5:
        no1=int(input("enter the number: "))
        no2=int(input("enter the number: "))
        print(no1,"//",no2,"=",no1//no2)

    elif operation ==6:
        print("Thanks for using my calculator")
        break
    else:
        print("Enter the correct operation")
       
                     
    
        
                      
                  
    
 
