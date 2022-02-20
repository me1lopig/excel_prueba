
# creación del libro
import openpyxl
wb = openpyxl.Workbook()

# nombre a una de las pestañas
hoja=wb.active
hoja.title="Valores"

productos = [
    ('producto_1', 'a859', 1500, 9.95),
    ('producto_2', 'b125', 600, 4.95),
    ('producto_3', 'c764', 200, 19.95),
    ('producto_4', 'd399', 2000, 49.95)]

# Crea la fila del encabezado con los títulos
hoja.append(('Nombre', 'Referencia', 'Stock', 'Precio'))

for producto in productos:
    # producto es una tupla con los valores de un producto 
    hoja.append(producto)

# guardado del archivo

wb.save('productos.xlsx')

