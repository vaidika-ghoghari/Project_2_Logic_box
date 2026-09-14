#========Project2. Logic box===========

print("\n\t" + "==="*10 + "  LOGIC BOX  " + "==="*10 +"\t")

#print  a welcome message for user
print("\n\nWelcome to the Pattern Generator and Number Analyzer ! ")

while True:
    #Give option for selection
    print("\nSelect an option : ")
    print("1. Generate a Pattern ")
    print("2. Analyze a Range of Numbers ")
    print("3. Exit  ")

    #taking user choice
    choice = int(input("Enter your choice : "))


    match choice:
        case 1:

            #taking a choice of pattern
            print("\n\nSelect a pattern :")
            print("1. Right-angle star Pattern ")
            print("2. Left-angle star Pattern ")
            print("3. Exit  ")

            #taking input of patterns
            pattern_choice = int(input("Enter your choice : "))
            
            #taking rows  from user
            
            match pattern_choice:
                case 1:
                        
                        row = int(input("\nEnter the number of Rows : "))
                        if row <= 0: 
                             print("\nInvalid input ! Rows must be greater than 0.")
                        else:
                             for i in range(1,row+1):
                                 for j in range(1,i + 1):
                                     print("*",end="   ")
                                 print()

                case 2:
                        row = int(input("\nEnter the number of Rows : "))
                        if row <= 0:
                            print("\nInvalid input ! Rows must be greater than 0.")
                        else:
                            for i in range(1, row + 1):
                                print("   " * (row - i) + "* " * i)

                case 3:
                        print("\nReturning to the Main Menu..." )
                        

                case _:
                        print("Invalid Choice !!!!!")  
                    
        case 2:
            while True:
                start = int(input("\nEnter starting number : "))
                end = int(input("Enter ending number : "))
                
                if end > start:
                    break
                    
                print("\nInvalid Range ! Ending number must be greater than starting number.")
            total = 0

            for i in range(start, end + 1):
                 if i == 0:
                    continue
                 elif i % 2 == 0:
                    print(f"Number {i} is Even.")
                 else :
                    print(f"Number {i} is Odd.")
                                
                 total += i

            print(f"\nSum of all numbers from {start} to {end} is : {total}")
            # In future adding aevrage and percentage of numbers
            pass       

        case 3:
            print("\nThank you for using Logic Box !")
            print("Exiting from the Program. Goodbye!")
            break
        

        case _:
            print("\nInvalid Choice !!!!!")
          
        

        
        
