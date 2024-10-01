def validar_especialidad():
    especialidades_validadas=("¨ programacion, administracion, contabilidad")
    while True:
        especialidad=input("Introduce tu especialidad(programacion, administracion, contabilidad)")
    if especialidad in especialidades_validadas:
        print(F"Especialidad [especialidad] validado correctamente")
    return especialidad 

def validar_genero():
    genero_valido =[" ¨Masculino", "Femenino", "No binario"]     
        
    while True:
        genero_valido=input("Introduce tu genero(Masculino, Femenino, No binario):") 
        if genero_valido in genero_valido:
         print("f genero [genero_valido] validado correctamente")
        return genero_valido
        else:
        print("Opcion no valida. Por favor, Intenta de nuevo")


def validar_mesada():
    mesada=0 #Inicialmente del rango deseado
    mesada=float(input("Ingrese mesada del alumno"))
    if mesada< 2000:
        print("La mesada es muy baja, Ingrese nuevamente")   
        if mesada>20000:
            print("La mesada es muy alta; Ingrese nuevamente")
        return mesada
    
def validar_nota():
    nota=0 #Inicialmente del rango deseado
    while nota((nota<1) or (nota>7)):
        nota=float(input("Ingrese nota del alumno:"))
        if nota < 1:
            print("nota muy pequeña, debe ser mayor o igual que 1.0")
            if nota> 7:
                print("nota muy grande, debe ser menor o igual a 7.0")
            return nota


def validar_edad():
    edad=-1 #Inicialmente del rango deseado
    while edad<= 0:
        edad=int(input("Ingrese un numero positivo:"))
        if edad <= 10:
            print("La edad no es positiva, Intentelo de nuevo.")
            if edad>=25:
                print("La edad es muy grande")
            return edad


def promedio(a,b,c):
    prom=(a+b+c)/3
    return prom