import random
import globales
import math
import json
import csv
import os
os.system("cls")


def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion


def leer_archivo_json(dir):
    try:
        with open(dir, 'r') as archivo: 
            return json.load(archivo) 
    except:
        return []

def guardar_archivo_json(dir, data):
    try:
        with open(dir, 'w') as archivo: 
            json.dump(data, archivo, indent=4)
    except:
        return []

def leer_archivo_csv(dir):
    try:
        with open(dir, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except:
        return []

def guardar_archivo_csv(dir, data, fieldnames):
    try:
        with open(dir, mode='w', newline='', encoding='utf-8') as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
            data_csv.writeheader()
            data_csv.writerows(data)
    except:
        return []


def listado_tabla(array, headers):
    col_widths = [max(len(header), 15) + 2 for header in headers]
    
    header_line = ' | '.join(f"{header.capitalize():^{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_line)
    print('-' * len(header_line))
    
    for data in array:
        row = ' | '.join(f"{str(data.get(header, '')):^{col_widths[i]}}" for i, header in enumerate(headers))
        print(row)


empleados = [
    "Luisa Morales",
    "Javier Torres",
    "Sofía Ramírez",
    "Martín Gutiérrez",
    "Valeria Castillo",
    "Diego Vargas",
    "Camila Ruiz",
    "Alejandro Medina",
    "Carolina Herrera",
    "Andrés Silva",
    "Paula Ortiz",
    "Gabriel Ramos"
]

def generar_sueldo(empleados):
    sueldos_empleados= []
    for empleado in empleados:
        sueldo = random.randint(900000,1500000)
        calculo_afp = math.floor(sueldo * 0.12)
        calculo_salud = math.floor(sueldo *0.07)
        sueldo_liquido = sueldo - calculo_afp - calculo_salud
        sueldos_empleados.append({
            "nombre": empleado,
	        "salud": calculo_salud,
	        "afp":	calculo_afp,
	        "sueldo_liquido": sueldo_liquido
        })
    return sueldos_empleados

def menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Asignar sueldos aleatorios")
    print("2. Ver estadísticas")
    print("3. Salir del programa")
    opcion = seleccionar_opcion(3)
    return opcion

def sueldo_mas_alto(empleados):
    max_valor = max(empleados, key=lambda x:x ['sueldo_liquido'])
    return max_valor ['nombre']

def sueldo_mas_bajo(empleados):
    min_valor = min(empleados, key=lambda x:x ['sueldo_liquido'])
    return min_valor ['nombre']


def promedio_empleados (empleados):
    total_sueldos = sum(empleado['sueldo_liquido']for empleado in empleados )
    promedio = total_sueldos / len(empleados)
    return promedio

def media_geometrica(empleados):
    sueldos_empleados = [empleado['sueldo_liquido'] for empleado in empleados]
    producto = 1
    for sueldo in sueldos_empleados:
        producto *= sueldo
    media_geom = producto ** (1 / len(empleados))
    return media_geom

def ver_estadisticas(empleados):
    print("Sueldo líquido más alto", sueldo_mas_alto(empleados))
    print("Sueldo líquido bajo", sueldo_mas_bajo(empleados))
    print("Promedio de sueldos líquido", promedio_empleados(empleados))
    print("Media geométrica sueldo líquido", media_geometrica(empleados))
    input("presione enter para cotinuar")



if __name__ == "__main__":
    opcion =''
    while opcion !=3:
        opcion = menu()
        if opcion == 1:
            empleados_valores = generar_sueldo(empleados)
            guardar_archivo_json('empleados.json', empleados_valores)
        elif opcion == 2:
            empleados_cargados = leer_archivo_json('empleados.json')
            if empleados_cargados:
                ver_estadisticas(empleados_cargados)
            else:
                print("no hay datos")
        elif opcion == 3:
            print("saliendo del programa...")
        else:
            print("opcion no valida")




