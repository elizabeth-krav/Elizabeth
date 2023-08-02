#The datetime module supplies classes for manipulating dates and times.
#Python's library datetime automatically counts leap years 

#using library datetime
from datetime import datetime

#this function will count how much time between now and user's dob
def a(z, y):
    return z - y

while True:
    
#using of class datetime
#atribute now() will show exactly time at the moment when program is used     
    now = datetime.now()
    print (datetime.now.year())
#taking user's dof and it will store it as data type string
    birthday=str(input("What is your birthday? (in DD/MM/YYYY) "))
    
#converting data type string to data type date with help of atribute strptime()
# '%d/%m/%Y' shows in which format date of birth will be showen ('%d/%m/%Y' means DD/MM/YYYY)
    birthdate=datetime.strptime(birthday, '%d/%m/%Y')
    '''while:
    if birthdate.year % 4 == 0 and birthdate.year % 100 != 0:
        birthdate.date = birthdate.date 
    elif birthdate.year % 100 == 0 and birthdate.year % 400 == 0:
        print(start)
    elif birthdate.year == datetime.now()
    birthdate.year += 1 '''
        
        
#(birthdate.year % 400) == 0                                 

#calling the function, this function uses arguments now and birthdate
#after counting atribute total_seconds() converts the result in seconds
    print('You live approximatly that many seconds ', a(now, birthdate).total_seconds())
   
#program asks a user if he/she wants to try again 
    s = input ('Restart? y/n: ')
#if yes then program will restart
    if s == 'y':
        continue
#in another case program will stop
    else:
        break
    
    


        



        


    
    
 

    



    
    



    
    


