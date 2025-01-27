import openpyxl

# Cadena de números
numeros_cadena = "124854197862111873594628755587963147899878963225114598777893111189757514796868228599642371258936145698666798982121235231"

# Separar los caracteres de la cadena y convertirlos a una lista
numeros_lista = list(numeros_cadena)
numeros_lista = [int(i) for i in numeros_lista]

# Crear un archivo de Excel
wb = openpyxl.Workbook()
sheet = wb.active

# Escribir los números en el archivo de Excel
for i in range(len(numeros_lista)):
    sheet.cell(row=i+1, column=1).value = numeros_lista[i]

# Guardar el archivo de Excel
wb.save("numeros.xlsx")
