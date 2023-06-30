# -*- coding: utf-8 -*-
"""IahnVera_PGY1121_004_V.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ogDLrG1uhyB2QYZfSXtVnQGqyV4cnxUG
"""

#Atención rápida RENAPER


personas = {}


#GRABAR
def grabar():
  print("Ingrese su número de DNI sin puntos y con guión")
  dni = (input())
  if validar_dni(dni):
    print("Numero de DNI no es válido, intente nuevamente")
    return
  print("Ingrese su nombre:")
  nombre = (input())
  if len(nombre) < 8:
    print("El nombre debe tener al menos 8 caracteres.")
    return
  print("Ingrese su apellido:")
  apellido = (input())
  print("Ingrese su edad:")
  edad = int(input())
  if edad < 0:
    print("Edad inválida, intentelo nuevamente")
    return
  print("Ingrese su país de nacimiento:")
  pais = (input())
  print("Ingrese su ciudad de nacimiento:")
  ciudad = (input())

  personas[dni] = {
          'nombre': nombre,
          'apellido': apellido,
          'edad': edad,
          'pais': pais,
          'ciudad': ciudad
      }
  print("Datos grabados exitosamente.")

#BUSCAR Y MOSTRAR
def buscar_mostrar_datos():
  print("Ingrese número de DNI de la persona que desea encontrar sin puntos y con guión:")
  dni=input()
  if dni in personas:
    persona = personas[dni]
    print("Información de la persona")
    print("Nombre: ",persona['nombre'])
    print("Apellido: ",persona['apellido'])
    print("Edad: ",persona['edad'])
    print("País de nacimiento: ", persona['pais'])
    print("Ciudad de nacimiento: ",persona['ciudad'])
    if persona['pais']=='Argentina':
      print("La persona es de nacionalidad argentina")
    else:
      print("La persona no es de nacionalidad argentina")
  else:
    print("No hay personas registradas con ese DNI")


#CERTIFICADOS
def  imprimir_certificados():
  for dni, persona in personas.items():
    print("Certificados de", persona['nombre'],persona['apellido'], "con DNI", dni)
    print("Certificado de Nacimiento")
    print("Certificado de Estado conyugal")
    if persona['pais'] == 'Argentina':
      print("Certificado de ciudadania argentina")
    print()

#ELIMINAR
def eliminar_datos():
  print("Ingrese el número de DNI:")
  dni = input()
  if dni in personas:
    del personas[dni]
    print("Se eliminaron los datos de la persona: ", dni)
  else:
    print("No hay personas registradas con ese DNI")


#VALIDAR DNI
def validar_dni(dni):
  if len(dni) != 10:
    return False

# Validación del numero del DNI - Ecuación citada, del ejercicio realizado ateriormente en clase

  partes = dni.split("-")
  numero = partes[0].replace(".","")
  verificador= partes[1].upper()
  suma = sum(int(digit) * (2 if i % 2 == 0 else 1) for i, digit in enumerate(numero[:-1]))
  resto = suma % 10
  verificador_esperado = str((10 - resto) % 10)
  return verificador == verificador_esperado

#MENU
def mostrar_menu():
  print("\tBienvenido a RENAPER")
  print("Seleccione una opción para continuar")
  print("1. Grabar")
  print("2. Buscar")
  print("3. Imprimir Certificados")
  print("4. Eliminar")
  print("5. Salir")
  print("Selecciona una opcion:")
  opcion = input()
  return opcion

#FUNCION PRINCIPAL
def main():
  while True:
    opcion = mostrar_menu()

    if opcion == '1':
      grabar()

    elif opcion == '2':
      buscar_mostrar_datos()

    elif opcion == '3':
      imprimir_certificados()

    elif opcion == '4':
      eliminar_datos()

    elif opcion == '5':
      print("Saliendo del sistema...")
      break
    else:
      print("Opción inválida. Intente nuevamente.")




#Ejecutar el sistema
main()