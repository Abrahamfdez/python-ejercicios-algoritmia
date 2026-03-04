# 1. Algoritmia e interacción con el usuario
# Ejercicio 1 Conversor de temperatura

"""
grados_celsius=float(input("DIME GRADOS CELSIUS"))

def pasar_a_Fahrenheit(c):
    return (c*9/5)+32

def pasar_a_Kelvin(c):
    return (c+273,15)

print(pasar_a_Fahrenheit(grados_celsius))
print(pasar_a_Kelvin(grados_celsius))


# Ejercicio 2 Números pares e impares

numeros=str(input("DIME NUMEROS SEPARADOS POR ESPACIO"))
array=list(map(int,numeros.split(" ")))
pares=filter(lambda a :a %2==0,array)
impares=filter(lambda a :a %2!=0,array)

impares=list(impares)
print(impares)

"""

# Ejercicio 3 Frecuencia de caracteres

"""
cadena= list(str(input("DIME UNA CADENA")))

char={}

for letra in cadena:
    char.setdefault(letra,0)
    char[letra]+=1

print(char)
"""

# Ejercicio 4 Calculadora básica

"""
num1=int(input("numero 1"))
operacion=str(input(("(+, -, *, /")))
num2=int(input("numero 2"))

match operacion:
    case "+":
        print(num1+num2)
        
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        try:
            print(num1/num2)
        except:
            print("ERROR DIVISION")
"""

# Ejercicio 5 Ordenacion de palabras

"""
frase=str(input("DIME PALABRA "))

palabras=frase.split(" ")

palabras.sort()

palabras.sort(key=len)

print(palabras)
"""

# Ejercicio 6 Números primos en un rango

"""


def numero_primo(numero):
    i=2
    while i <= numero-1:
        if numero%i==0:
            return False
        i+=1
    return True

def rango_primos(nu1,nu2):
    if nu1 >num2:
        return True
    else:
        if numero_primo(nu1):
            print(f"{nu1} es primo")
    rango_primos(nu1+1,nu2)

num1=int(input("numero 1"))
num2=int(input("numero 2"))
rango_primos(num1,num2)

"""

# FIBBONUCCI

"""
def fibunuchi(num):
    if num<1:
        return 0
        
    if num==1:
        return 1
    return fibunuchi(num-1)+fibunuchi(num-2)

for i in range(0,50):
    print(fibunuchi(i))

"""

# invertir cadena

"""
cadena="HOLA MUNDO!"
cadena2=""
for letra in range(len(cadena),0,-1):
    cadena2+=cadena[letra-1]

print(cadena2)
"""

# Ejercicio 7 Gestión de notas

"""
notas=[]
list(notas)
media=0

entrada=""
while(entrada!="fin"):
    entrada=input("DIME NOTAS(fin para terminar): ")
    try:
       
        notas.append(int(entrada))
    except:
        print(" ")


print(notas) 
for nota in notas:
        media=nota+media

media=media/(len(notas))
print(f"media: {media}")
notas.sort()
print(f"Nota mas alta: {notas[len(notas)-1]}")
notas.reverse
print(f"Nota mas baja: {notas[0]}")

"""

# Ejercicio 8 JUEGO DE ADIVINANZAS

"""
import random
ran=random.randint(1,100)


while (True):
    adiv=int(input("DIME UN NUMERO DEL 1-100"))
    if ran==adiv:
        print("ADIVINASTE")
        break
    elif ran>adiv:
        print(f"EL NUMERO ES MAYOR A {adiv}")
    else:
        print(f"EL NUMERO ES MENOR A {adiv}")
"""
#                       2. Secuencias y diccionarios

# Ejercicio 9 Diccionario de frecuencias de palabras

"""
frase= input("DIME UNA FRASE: ")
diccionario={}
for letra in frase:
    diccionario.setdefault(letra,0)
    diccionario[letra]+=1
print(diccionario)
"""

# Ejercicio 10 Tuplas y coordenadas
"""
import math 

x1=int(input("DIME X"))
y1=int(input("DIME Y"))

x2=int(input("DIME X2"))
y2=int(input("DIME Y1"))

cateto1=x1-x2
cateto2=y1-y2

resultado=math.sqrt((math.pow(cateto1,2)+math.pow(cateto2,2)))

print(resultado)
"""

# Ejercicio 11 Diccionario inverso

"""
import random

frase= input("DIME UNA FRASE: ")
diccionario={}
for letra in frase:
    diccionario.setdefault(letra,random.randint(1,100))
    diccionario[letra]+=1
print(diccionario)

diccionario_inverso={}

for k,v in diccionario.items():
    diccionario_inverso.setdefault(v,k)
print(diccionario_inverso)
"""

# Ejercicio 12 Lista de diccionarios (agenda)
"""

contactos={}
while(True):
    menu=input(" a para añadir / b para buscar [CONTACTOS] [e para salir]")
    if(menu=="a"):
        telefono=0
        nombre=""
        while(telefono  in contactos):
            nombre=input("DIME NOMBRE: ")
            telefono=input("DIME TELEFONO: ")

        contactos.setdefault(telefono,nombre)
    elif(menu=="b"):
        nombre=input("DIME NOMBRE: ")
        busqueda=[k for k,v in contactos.items() if v==nombre]
        print(busqueda)
    elif(menu=="e"):
        break
        
"""
#                               3. Funciones

# Ejercicio 13 Funciones simples

"""
def is_par(n):
    if(n%2==0):
        return True
    return False
"""
# Ejercicio 14 Funciones con retorno múltiple

"""
def calculos(n):
    media=0
    lista=[]
    list(n)
    for numeros in n:
        media=numeros+media
    lista.append(media/len(n)-1)
    n.sort
    lista.append(n[0])
    lista.append(n[len(n)-1])
    return lista
print(calculos([1,2,3,4,5]))
"""

# Ejercicio 15 Uso de functools.reduce

"""
from functools import reduce

lista=[2,3,4]

liosta2=reduce(lambda x,y: x*y ,lista)
print(liosta2)

"""

# Ejercicio 16 Módulos propios

"""


def utilidades(nombre):
    print(f"HOLA {nombre}")

"""

#                                                               4. Programación Orientada a Objetos
# Ejercicio 17 Clase Rectángulo

"""
class rectangulo:

    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    
    
    
    def calcular_area(self):
        return self.alto* self.alto 
    
    def calcular_perimetro(self):
        return 2* (self.alto+self.alto) 
    

r1=rectangulo(20,40)
print(r1.calcular_area())
print(r1.calcular_perimetro())

"""

# Ejercicio 18 Clase Cuenta

"""

class Cuenta:
    def __init__(self,saldoInicial):
        self.saldoInicia=saldoInicial

    def ingresar(self,cantidad):
        self.saldoInicia+=cantidad

    def retirar(self,cantidad):
        self.saldoInicia-=cantidad

    def mostrarSaldo(self):
        print(f"Tu saldo es de: {self.saldoInicia}")

c1=Cuenta(1200)
c1.mostrarSaldo()

"""

# Ejercicio 19 Jerarquía de Empleados
"""

class Gerente:
    def __init__(self,departamento,Programador):
        self.departamento=departamento
        self.Programador=Programador

    @property
    def departamento(self):
        return self._departamento
    
    @description.setter
    def departamento(self,departamneto):
        self._departamento=departamneto
    
    @property
    def Programador(self):
        return self._Programador
    
    @description.setter
    def Programador(self,Programador):
        self._Programador=Programador
    
    def __str__(self):
       return self.departamento+", "+self.Programador



class Empleado(Gerente):

    def __init__(self, departamento, Programador,nombre,sueldo):
        super().__init__(departamento, Programador)
        self.nombre=nombre
        self.sueldo=sueldo
    
    @property
    def nombre(self):
        return self.nombre
    
    @description.setter
    def nombre(self,nombre):
        self.nombre=nombre

    @property
    def sueldo(self):
        return self.sueldo
    
    @description.setter
    def sueldo(self,sueldo):
        self.sueldo=sueldo
    
    def __str__(self):
        return super().__str__()+", "+self.sueldo+", "+self.nombre

"""
# Ejercicio 20 Sistema de biblioteca (clases + composición)

"""
class Libro():
    def __init__(self,titulo,autor):
        self.__titulo=titulo
        self.__autor=autor

    @property
    def titulo(self):
        return self.__titulo
    @property
    def autor(self):
        return self.__autor
    
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo=titulo
    
    @autor.setter
    def autor(self,autor):
        self.__autor=autor
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
class Biblioteca:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__Libros=[]
    @property
    def nombre(self):
         return self.__nombre
    
    @property
    def Libros(self):
         return self.__Libros
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @Libros.setter
    def Libros(self,libros):
        self.__Libros=libros
    
    def addLibro(self,libro):
        self.__Libros.append(libro)

    def searchLibro(self,titulo):
        return [libro for libro in self.Libros if libro.titulo==titulo]
        
    def listarLibros(self):
        for i,libro in enumerate(self.Libros,1):
            print(f"{i}. {libro}")

l1 = Libro("El Quijote", "Cervantes")
l2 = Libro("Cien años de soledad", "García Márquez")

b = Biblioteca("Central")
b.addLibro(l1)
b.addLibro(l2)
b.listarLibros()

for i,libro in enumerate(b.searchLibro("El Quijote"),1):
            print(f"{i}. {libro}")
"""
            
#  Lectura y escritura de ficheros (texto y JSON) 
# Ejercicio 21 Contador de líneas

"""
new_fich=open("lineas.txt","r")
linea=new_fich.readline()
contador=0

while linea!="":
    contador+=1
    contador_linea=0
    array=linea.split()
    print(f" {len(array)} palabras en linea: {contador}")
    linea=new_fich.readline()
new_fich.close()
"""

# Ejercicio 22 Registro de usuarios en archivo
 
"""
new_fich=open("login.txt","w")
nombre=input("DIME NOMBRE: ")
correo=input("DIME EMAIL")
new_fich.write(f"{nombre} {correo}")
"""

# Ejercicio 23 Exportación a JSON 24 Lectura de JSON
"""
import json
titulo=input("DIME TITULO: ")
estado=input("DIME ESTADO: ")

tarea={
    "titulo":titulo,
    "estado":estado
}

with open("tareas.json","r") as file:
    text=file.read()
    result=json.loads(text)

resultadoBusqueda=list(filter(lambda x: x["estado"]=="finalizado",result))
print(resultadoBusqueda)
result.append(tarea)

with open("tareas.json","w") as file:
    json.dump(result,file)
"""

#  6. Conexión con MongoDB
# Ejercicio 25 Exportación a JSON

"""from pymongo import MongoClient
basededatos = MongoClient ('mongodb://root:abc123.@localhost:27017')
db = basededatos["prueba_bd"]
bicicletas=db["bicicletas"]


print(bicicletas.find_one({ "nombre": 'bici_verde',
    "marchas": 26,
    "caracteristicas": {
        "suspension": 'KW'
    }}))
      6. Conexión con MongoDB
# Ejercicio 25 Exportación a JSON

from pymongo import MongoClient
basededatos = MongoClient ('mongodb://root:abc123.@localhost:27017')
db = basededatos["prueba_bd"]
print(basededatos.list_database_names())
"""
# Ejercicio 26 Inserción de documentos
"""
lista_alumnos = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 7.2},
    {"nombre": "Marta", "edad": 21, "nota": 9.1},
    {"nombre": "Carlos", "edad": 23, "nota": 6.8},
    {"nombre": "Sofía", "edad": 20, "nota": 7.9}
]
"""
# Ejercicio 27 Consulta con filtros
"""
alumnos=db["alumnos"]
alumnos.insert_many(lista_alumnos)         

busqueda=alumnos.find({"nota":{"$gt":7}})
for alumno in busqueda:
    print(alumno)
"""
# Ejercicio 28 Actualización y eliminación
"""
alumnos.update_many({"nombre":"Ana"},{"$set":{"edad":30}})
alumnos.delete_many({"nota":{"$lte":5}})
for a in alumnos.find():
    print(a)
"""
