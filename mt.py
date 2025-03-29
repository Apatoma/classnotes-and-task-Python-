# mt = media temperaturas
#empieza el contador desde 0
cuentatemp = 0
sumatemp = 0

while True:
    temp = input("Introduce la temperatura (o escribe 'fin' para terminar): ") 
    if temp.lower() == 'fin': #tem.lower() convierte a minusculas el input, si es fin se termina el bucle y ya calcula la media.
        break #se termina el bucle
    else:
        temp = float(temp)
        sumatemp += temp
        cuentatemp += 1 #suma la temperatura y cuenta las temperaturas introducidas

if cuentatemp > 0:
    media = sumatemp / cuentatemp
    print("La media de las temperaturas es:", media) #se calcula la media de las temperaturas introducidas
else:
    print("No se introdujeron temperaturas.") #si no se introdujeron temperaturas, se avisa al usuario.

