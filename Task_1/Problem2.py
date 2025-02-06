import datetime  

day = int(input("Day: "))  
month = int(input("Month: "))  
year = int(input("Year: "))  
today = datetime.date(year, month, day)  

next_week = today + datetime.timedelta(days=7)  

print("Day:", next_week.day, "Month:", next_week.month, "Year:", next_week.year)
