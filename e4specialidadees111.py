# Calcular el promedio de 3 edades
# Calcular el promedio de 3 notas
# Calcular el promedio de 3 mesadas

nombre= [0,0,0]  
especialidad=[0,0,0] 
notas=[0,0,0]
edad=[0,0,0]
mesada= [0,0,0]

for i in range(0,3,1): #0, 1, 2
print ("DATOS ALUMNO",i+1)
nombre(i)=input("INGRESE NOMBRE DEL ALUMNO:")
especialidad(i)= validar_especialidad()

#especialidad =validar_especialidad()
#edad1=validar_edad()
#nota1=validar_nota()
mesada1=int(input("Ingrese mesada del alumno:"))
print("")
 
for i in range(0,3,1):
    print("ALUMNO")
print("ALUMNO",i+1":",especialidad)
def promedio(a,b,c):
    prom=(a+b+c)/3
    return prom

def validar_edad():
    edad=-1 #Inicialmente del rango deseado
    while edad<= 0:
        edad=int(input("Ingrese un numero positivo:"))
        if edad <= 10:
            print("La edad no es positiva, Intentelo de nuevo.")
            if edad>=25:
                print("La edad es muy grande")
            return edad


def validar_nota():
    nota=0 #Inicialmente del rango deseado
    while nota((nota<1) or (nota>7)):
        nota=float(input("Ingrese nota del alumno:"))
        if nota < 1:
            print("nota muy pequeña, debe ser mayor o igual que 1.0")
            if nota> 7:
                print("nota muy grande, debe ser menor o igual a 7.0")
            return nota
        
        
def validar_mesada():
    mesada=0 #Inicialmente del rango deseado
    mesada=float(input("Ingrese mesada del alumno"))
    if mesada< 2000:
        print("La mesada es muy baja, Ingrese nuevamente")   
        if mesada>20000:
            print("La mesada es muy alta; Ingrese nuevamente")
        return mesada
    
    
    
    def validar_genero():
        genero_valido =[" ¨Masculino", "Femenino", "No binario"]     
        
        while True:
            genero_valido=input("Introduce tu genero(Masculino, Femenino, No binario):") 
            if genero_valido in genero_valido:
                print("f genero [genero_valido] validado correctamente")
                return genero_valido
            else:
                print("Opcion no valida. Por favor, Intenta de nuevo")


def validar_especialidad():
    especialidades_validadas=["¨ programacion, administracion, contabilidad"]
    while True:
        especialidad=input("Introduce tu especialidad(programacion, administracion, contabilidad)")
    if especialidad in especialidades_validadas:
        print (f "Especialidad [especialidad] validado correctamente")
    return especialidad 
    else:
        print(Opcion no valida, Por favor, intenta de nuevo)



print("Bienvenido septiembre")
print("")
# Alumno 1
print("Datos alumno 1")
nombre=input("Ingrese nombre del alumno:")
edad1=int(input("Ingrese edad del alumno:"))
edad1=validar_edad()
nota1=float(input("Ingrese nota del alumno:"))
nota1=validar_nota()
mesada1=int(input("Ingrese mesada del alumno:"))
mesada1=validar_mesada()

# Alumno 2
print("Datos alumno 2")
nombre=input("Ingrese nombre del alumno:")
edad=int(input("Ingrese edad del alumno:"))
edad2=validar_edad()
nota2=float(input("Ingrese nota del alumno:"))
nota2=validar_nota()
mesada2=int(input("Ingrese mesada del alumno:"))
mesada2=validar_mesada()

# Alumno 3
print("Datos alumno 3")
nombre=input("Ingrese nombre del alumno:")
edad=int(input("Ingrese edad del alumno:"))
edad2=validar_edad()
nota3=float(input("Ingrese nota del alumno:"))
nota3=validar_nota()
mesada3=int(input("Ingrese mesada del alumno:"))
mesada3=validar_mesada()

# Calculos
prom_e=promedio(edad,edad,edad)
prom_n=promedio(nota1,nota2,nota3)


# Respuestas
print("El promedio de las edades de los 3 alumnos es:", prom_e)
print("El promedio de las notas de los 3 alumnos es:", prom_n)