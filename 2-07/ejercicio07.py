from guizero import App, TextBox, PushButton, Text

# Función para calcular la suma de los cuadrados de los números pares
def calcular_suma_cuadrados():
    valor = int(valor_input.value)
    numeros_pares = [x for x in range(0, valor + 1) if x % 2 == 0]
    suma_cuadrados = sum([x ** 2 for x in numeros_pares])
    resultado.value = f"La suma de los cuadrados de los números pares entre 0 y {valor} es: {suma_cuadrados}"

# Crear una aplicación GUI
app = App("Suma de Cuadrados de Números Pares", width=300, height=200)

# Cuadro de texto para ingresar un valor
valor_input = TextBox(app, width=10)
Text(app, text="Ingrese un valor:")

# Botón para calcular la suma de cuadrados
calcular_button = PushButton(app, text="Calcular Suma de Cuadrados", command=calcular_suma_cuadrados)

# Etiqueta para mostrar el resultado
resultado = Text(app, text="", size=12)

# Iniciar la aplicación
app.display()