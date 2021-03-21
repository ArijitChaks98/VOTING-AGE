Birthyear = int(input("BirthYear\n"))
Birthmonth = int(input("BirthMonth\n"))
Birthdate = int(input("BirthDate\n"))
Currentyear = int(input("CurrentYear\n"))
Currentmonth = int(input("CurrentMonth\n"))
Currentdate = int(input("CurrentDate\n"))
Year = abs(Birthyear-Currentyear)
Month = abs(Birthmonth-Currentmonth)
Date = abs(Birthdate-Currentdate)
VotingAge = 18
if(Year>VotingAge):
    print("THIS IS YOUR AGE\n",Year, Month, Date)
    print("YOU ARE ELEGIBLE FOR VOTING!\n")
else:
    print("THIS IS YOUR AGE\n",Year, Month, Date)
    print("YOU ARE NOT ELEGIBLE FOR VOTING!\n")