import random
year= random.randint(1857,2019)
print(year)
if(year%400==0 and year%100!=0 or year%4==0):
    print("Given Year is Leap Year")
else:
    print("Given year is not leap Year")
    
