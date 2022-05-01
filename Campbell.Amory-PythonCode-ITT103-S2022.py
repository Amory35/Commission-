#Author: Amory Campbell
#Date Created: April 25, 2022
#Course: ITT103
#Purpose: This program was developed for the calculation of the commission rate to be paid to salespersons based on sales performance.

sal_person = int(input("Enter salesperson number: "))
sal_amount = float(input("Enter sales amount: "))
Class = float(input("Enter your class: "))

if Class == 1: #If class is 1

        if sal_amount <= 1000: #If sale amount less than or equal to 1000
                com_rate = (0.06 * sal_amount) #6% comission 

        elif sal_amount > 1000 and sal_amount < 2000: #If sale amount is greater than 1000 but less than
                                                                                                        #2000
                com_rate = (0.07 * sal_amount) #7% comission

        else:
                com_rate = (.1 * sal_amount) #10% comission

elif Class == 2: #If class is 2
        #Same conditions as above, only the comission percentage is different
        if sal_amount < 1000:
                com_rate = (.04 * sal_amount)

        else:
                com_rate = (0.06 * sal_amount)

elif Class == 3: #If class is 3
        com_rate = (0.045 * sal_amount)

else:#If any invalid class is entered
        print("Please enter a valid class")
#The try block tries to print com_rate
try:
        print("Saleperson ", sal_person, "Commission Rate ", com_rate)
except:
        pass
