import subprocess as sp

# Variable globlase
nombre_archivo = 'retults.txt'

# determina si el numero dado es primo
def es_primo(numero):

    # Casos especiales
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False

    # Iterar divisores impares hasta la raiz cuadrada de numero
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True

# Valida si la entrada es un numero
def es_numero(entrada):
    try:
        int(entrada)
        return True
    except ValueError:
        return False

# Obtener un numero del usuario y validar si es numero y positivo si no lo es preguntar por un nuevo numero
def obtener_numero(rango):
    while True:
        entrada = input(f"Ingresa el valor para el limite {rango}: ")
        if es_numero(entrada):
            entrada = int(entrada)
            if entrada >= 1:
                return entrada
        else:
            print('Valor ingresado no aceptado, Por favor ingreas un valor valido.')

# validar si el valor inferior es menor al valor superior
def validar_rango(valor_inferior, valor_superior):
    if valor_inferior >= valor_superior:
        return False
    return True

# Preguntar por el rango para buscar lo numero primos
def obtener_rango():
    rango = False
    # Seguir preguntando por un rango si no se ingresan datos validos
    while not rango:
        rango_inferior = obtener_numero('inferior')
        rango_superior = obtener_numero('superior')
        rango = validar_rango(rango_inferior, rango_superior)
        # si el rango no es valido preguntar si quiere intentar de nuevo o usar un rango por defecto
        if not rango:
            print('Rango invalido!\nSe usara el rango por defecto(1-250)')
            reintentar = str(input('Quieres intentar ingresar un rango valido?(si/no): '))
            if reintentar == 'no':
                rango_inferior = 1
                rango_superior = 250
                rango = True

    return rango_inferior, rango_superior

# Hacer una lista con los numero primos encontrados dentro del rango
def listar_numeros_primos(rango_inferior, rango_superior):
    primos = []
    for numero in range(rango_inferior, rango_superior + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Obtenemos la ruta en donde esta corriendo el programa
def obtener_ruta():
    return sp.run('pwd', capture_output = True, text = True).stdout.strip()

# Creamos el archivo para guardar la lista de numeros primos
def crear_archivo(ruta_completa, nombre_archivo):
    # Verificamos si el archivo existe
    resultado = sp.run(['find', ruta_completa, '-name', nombre_archivo], capture_output = True, text = True)
    # Si no existe lo creamos
    if not resultado.stdout:
        sp.run(['touch', ruta_completa], check = True)
        print(f"El archivo {nombre_archivo} ha sido creado en {ruta_completa}.")
    # si existe, notificamos en consola
    else:
        print(f"El archivo {nombre_archivo} ya existe.")
    # Creado o existente, nos aseguramos que tengo los permisos para escribir en el archivo    
    sp.run(['chmod', '644', ruta_completa], capture_output = True, text = True)

# Agregamos la lista de numeros primos al archivo
def agregar_lista(lista, rango,ruta):
    try:
        with open(ruta, 'a') as archivo:
            archivo.write(f"Rango: {rango}\n")
            # Si es el ultimo elemento de la lista cambia el formato 
            for numero in lista:
                if lista.index(numero) == len(lista) - 1:
                    archivo.write(f"{numero}: {len(lista)}\n\n")
                else:
                    archivo.write(f"{numero}, ")
            print(f"Los numeros han sido agregados al archivo en la ruta: {ruta}")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

# Funcion principal 
if __name__ == "__main__":
    print('Bienvenido! \nPara saber los numeros primos dentro de un rango proporciona los siguientos datos: ')
    rango_inferior, rango_superior = obtener_rango()
    print(f"\nEl rango a usar es {rango_inferior} - {rango_superior}")
    rango = f" {rango_inferior} - {rango_superior}"
    primos = listar_numeros_primos(rango_inferior, rango_superior)
    print(f"El numero de primos encontrados dentro del rango dado es de {len(primos)} numeros primos:")
    print(primos, end = '\n\n')
    ruta = obtener_ruta()
    ruta_completa = f"{ruta}/{nombre_archivo}"     
    crear_archivo(ruta_completa, nombre_archivo)
    agregar_lista(primos, rango, ruta_completa) 
