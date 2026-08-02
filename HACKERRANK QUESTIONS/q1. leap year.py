def is_leap(year):
    leap = False
    if(year % 4 == 0 ):
        print("True")
    
    return leap
    
year = int(input())
print(is_leap(year))