#Escriba un programa que imprima los nombres de una lista que tenga exactamente 5 letras, pero imprime cada name en mayus
nombre = ["alex","pacho","tijuana","santiago","ruperta"]
for nombre in (nombre):
    if len(nombre) == 5:
        print (nombre.upper())