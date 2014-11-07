#Nick Lee
#calendar program






def print_slash(numDaysInMonth,month,year):    #function that pints dates this fashion 1/1/2000
    for day in range(1,numDaysInMonth+1):
        if day == 1 and month == 1:
            print("New Year's Day: " + str(month) + "/"+ str(day) +"/" + str(year))

        elif day == 14 and month == 2:
            print("Valentine's Day: " +str(month) + "/"+ str(day) +"/" + str(year))

        elif day == 1 and month == 4:
            print("April Fool's Day: " +str(month) + "/"+ str(day) +"/" + str(year))

        elif day == 4 and month == 7:
            print("Independence Day: " +str(month) + "/"+ str(day) +"/" + str(year))    
            
        elif day == 31 and month == 10:
            print("Halloween: " +str(month) + "/"+ str(day) +"/" + str(year))
        
        else:
            print(str(month) + "/"+ str(day) +"/" + str(year))

        



def print_days(numDaysInMonth,month,year):   #function that prints dates in this factoin Janurary 2, 2000
    for day in range(1,numDaysInMonth+1):

        if day == 1 and month == "January":
            print("New Year's Day: "+ month + " "+str(day) + ", " + str(year))

        elif day == 14 and month == "February":
            print("Valentine's Day: " + month + " "+str(day) + ", " + str(year))

        elif day == 1 and month == "April":
            print("April Fool's Day: " + month + " "+str(day) + ", " + str(year))

        elif day == 4 and month == "July":
            print("Independence Day: " + month + " "+str(day) + ", " + str(year))
            
        elif day == 31 and month == "October":
            print("Halloween Day: " + month + " "+str(day) + ", " + str(year))
        
        else:
            print(month + " "+str(day) + ", " + str(year))





         


def leap(year):    #leap year boolen function returns true or false based on if year is leap year


    if year%400 == 0:
        return True
    
    elif year%100==0 and year%400!= 0:
        return False

    elif year%4==0 and year%100 != 100:
        return True

    else:
        return False    
    

        

     
      
            





         

def func():

    first_year = int(input("What year would you like to start?\n"))	 #input set to varibale for users desired start year

    while first_year < 0:		                                # loop for if the user enterned a negative number, it will repeat the question		
        first_year = int(input("Please enter a nonnegative year. What year would you like to start?\n"))		#while loop to make sure year is a valid positive year

    print("You have chosen the year " + str(first_year) + " as your starting year")                                 #statement showing what year user has picked

    end_year = int(input("What would you like to print up to?\n")) 	    

    while end_year < 0 or end_year < first_year:                            #while loop for if the second valye is negative or if it's lower than the first value
    	end_year = int(input("Please enter a nonnegative year or year greater than your first. What year would you like to end with?\n"))

    print("You have chosen the year " + str(end_year) + " as your ending year")   #showing user what they chose for end date

    format = input("What date format do you want to print? Ex. with slashes ' 1/1/2000 ' or by printed month 'Januaray, 1, 2000' ? Please enter '-' for slashes or 'print' for printed month." )# ask used what format they want to use





    
  
    
    if format == "print":         #if user choose print it will exucute the follwoing code
        
        for year in range(first_year,end_year+1):
            for month in ["January","February","March","April","May","June","July","August","September","October","November","December"]:
            
                if month == "January" or month == "March" or month == "May" or month == "June" or month == "July" or month == "August" or month == "October" or month == "December":
                     x = 31
                     print_days(x,month,year)   
    
                elif month == "September" or month == "April" or month == "June" or month == "November":
                    x = 30
                    print_days(x,month,year)
    
                elif month == "February":

                    check = leap(year)   #this brings up the boolean function

                    if check == True:    #if true, then a leap year
                        x = 29
                        print_days(x,month,year)
                    
                    elif check == False:   #if flase, then a normal year
                
                        x = 28
                        print_days(x,month,year)

                    else:
                        x = 29
                        print_days(x,month,year)
                        
                    

            

    elif format == "-":        #if user choose the - way 
        print("ok")
        for year in range(first_year,end_year+1):
            for month in range(1,13):   #ragne of months, 13 to get in 12 
            
                if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10  or month == 12 :
                     x = 31
                     print_slash(x,month,year)   
    
                elif month == 9 or month == 4 or month == 6 or month == 11:
                    x = 30
                    print_slash(x,month,year)
    
                elif month == 2:

                    check = leap(year)  #same as above. checks if year is leapyear or not 
                
                    if check == True:    
                        x = 29
                        print_slash(x,month,year)
                    
                    elif check == False:
                        x = 28
                        print_slash(x,month,year)

                    else:
                        x = 28
                        print_slash(x,month,year)
                        


                    
    else:
        format = input("What date format do you want to print? Ex. with slashes ' 1/1/2000 ' or by printed month 'Januaray, 1, 2000' ? Please enter '-' for slashes or 'print' for printed month.") 

func()      #calls program
