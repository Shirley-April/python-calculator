

def calculate():# function that perform our calculation
    
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    

#ask for input and store it in operation variable
    operation  = input("Enter a choice (1/2/3/4) ")
    
    
    try:
      
       number_1 = float(input("Enter a number: "))
       number_2 = float(input("Enter a number: "))
       operarion != float or int
     
    except:  
      print(" Invalid choice")
         
    
 #calc addition 
    if operation == "1":

        print("{} + {} = ".format(number_1,  number_2))
        print(number_1 + number_2)
        
#calc subtraction
    elif operation == "2":
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)
        
 # calc multiplication
    elif operation == "3":
        print("{} * {} = ".format(number_1,  number_2))
        print(number_1 * number_2) 
        
# calc division
    elif operation == "4":
        print("{}  / {} = ".format(number_1, number_2))
        print(number_1 / number_2)

    else:  
        print("Invalid operator! ")
    again()# add again() here to ask user if theywant to continue

def again():# function to ask user if they want to continue
    print("Press Y to continue\nPress N to stop")
    
    #ask user for input
    calc_again = input()
    if calc_again.upper() == "Y":
        calculate()# if "Y" continue
    elif calc_again.upper() == "N":
        print("BYE")#if "N" end program
    else:
        again()# other value run function again
calculate()