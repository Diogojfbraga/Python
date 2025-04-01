def is_leap_year(year):   
    
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)):
        return print(f"{chosen_year} is a leap year")
    else:
        return print(f"{chosen_year} is not a leap year")
        
chosen_year = int(input('Chose a year: '))      
is_leap_year(chosen_year)