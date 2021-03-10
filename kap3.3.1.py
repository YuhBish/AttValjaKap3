import math
min=float(input("Hur många minuter ringer du telefon per månad? "))  

if min<=33:
    print("Välj KONTANT abbonemanget")    
elif min<=66:
    print("Välj NORMAL abbonemanget")
else:
    print("Välj PLUS abbonemanget")    
