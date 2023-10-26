#Una empresa desea saber el sueldo total de una persona bajo los siguientes rubros: 
#percepciones, sueldo base, 5% de canasta básica, 3% de prima de antigüedad y deducciones, 
#si el salario base excede los 10,000 mil pesos el impuesto es de 30% y si es menos sera el 20%, 
# indique cuanto es el total de la nomina a pagar y cuantos son los impuestos que el patrón 
#tiene que pagarle al SAT.

from guizero import App, Box, Text, TextBox, PushButton

# Variables globales
cantidad_empleados = 0
suma_sueldos = 0
suma_impuestos = 0
contador = 0

# Función para pedir el salario del empleado
def pedir_salario():
    global contador, suma_sueldos, suma_impuestos
    salario_base = float(salario_box.value)
    
    # Validar si el salario excede los 10,000 pesos
    if salario_base > 10000:
        impuestos = salario_base * 0.3
    else:
        impuestos = salario_base * 0.2
    
    canasta_basica = salario_base * 0.05
    prima_antiguedad = salario_base * 0.03
    
    sueldo_total = salario_base - impuestos + canasta_basica + prima_antiguedad
    
    suma_sueldos += sueldo_total
    suma_impuestos += impuestos
    contador += 1
    
    if contador < cantidad_empleados:
        resultado.value = f"Llevamos {contador} empleado(s) calculado(s)."
    else:
        resultado.value = f"Nómina total a pagar: {suma_sueldos:.2f}\nImpuestos totales a pagar al SAT: {suma_impuestos:.2f}"

# Función para pedir la cantidad de empleados
def pedir_cantidad_empleados():
    global cantidad_empleados
    cantidad_empleados = int(cantidad_empleados_box.value)
    cantidad_empleados_box.disable()
    siguiente_empleado()

# Función para pasar al siguiente empleado
def siguiente_empleado():
    salario_box.clear()
    salario_box.enable()
    calcular_button.enable()
    resultado.value = "Ingrese el salario del empleado."

# Crear una aplicación GUI
app = App("Calculadora de Nómina", width=400, height=300)

# Crear una caja para organizar elementos
box = Box(app, layout="grid")

# Etiqueta y cuadro de texto para ingresar la cantidad de empleados
Text(box, text="Cantidad de empleados:", grid=[0, 0])
cantidad_empleados_box = TextBox(box, grid=[1, 0])
cantidad_empleados_button = PushButton(box, text="Aceptar", command=pedir_cantidad_empleados, grid=[2, 0])

# Etiqueta, cuadro de texto y botón para ingresar el salario
Text(box, text="", grid=[0, 1])
salario_box = TextBox(box, grid=[1, 1])
calcular_button = PushButton(box, text="Calcular Salario", command=pedir_salario, grid=[2, 1])
calcular_button.disable()
salario_box.disable()

# Etiqueta para mostrar el resultado
resultado = Text(box, text="", grid=[0, 2, 3, 1])

# Iniciar la aplicación
app.display()