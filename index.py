import os
import time

def conv(c):
    farenheit = 9/5 * c + 32
    return farenheit

os.system("cls")
while True:
    try:
        celcius = float(input("Ingrese la temperatura en celcius: "))
    except Exception:
        os.system("cls")
        print("Por favor ingrese la temperatura correctamente")
        continue
    else:
        farenheit = conv(celcius)
        print("La Temperatura en farenheit es: ",farenheit)
        time.sleep(3)
        break

    
    
    
    
    
    
    
        

    


