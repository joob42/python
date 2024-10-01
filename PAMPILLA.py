def validar_sueldo():
    sueldo=0
    while((sueldo<1000000) or (sueldo>17000000)):
        try:
            sueldo=int(input("Ingrese sueldo del artista: "))
            if sueldo < 1000000:
                print("Sueldo muy bajo, debe ser mayor o igual que 1.000.000, Intente nuevamente")
                if sueldo > 17000000:
                    print ("Sueldo muy alto, debe ser menor o igual que 17.000.000, Intente nuevamente")
        except ValueError:
            print("Debe escribir el sueldo como entero")
            print("")
            return sueldo
        
        
def validar_dia():
    dias_validos=["17-09", "18-09", "19-09", "20-09"]
    
    while True:
        dia=input("Seleccione fecha del show(17-09, 18-09, 19-09, 20-09): ")
        if dia in dias_validos:
            print(f"Fecha "[dia]" validada correctamente.")
            print("")
            return  dia 
        else:
            print("fecha no valida. Por favor, intenta nuevamente.")
            
def validar_positivo(numero):
    if numero > 0:
        return True
    else :
        return False
    
#Arreglos o Array
nombre = []            
apellido = []
apodo = []
dia = []
sueldo = []

print("Bienvenido a la pampilla insuco")
print("")


n=int (input("Ingrese cantidad de artistas: ")) 
print("")
validar_positivo(n)
for i in range(n):
    print("artista", i+1)
    nombre.append(input("Ingrese nombre: "))
    apellido.append(input(("Ingrese apellido del artista: ")))
    apodo.append(input(("Ingrese apodo del artista: ")))
    sueldo.append(validar_sueldo())
    dia.append(validar_dia())
    print("")
    #CICLO FOR  PARA IMPRESION DE DATOS
    for i in range (n):
        print(apodo[i])
        print(f"El nombre del artista es[nombre[i]]")
        print(f"El apellido del artista es[apellido[i]]")
        print(f"Su sueldo es[sueldo[i]]")
        print(f"Se presentara en la pampilla el[dia[i]]")
        print("")
