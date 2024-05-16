import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np



# Definir los widgets para los parámetros
C0_widget = widgets.FloatText(description='C0:', value=620)
C_widget = widgets.FloatText(description='C0:', value=20)
I_widget = widgets.FloatText(description='I:', value=220)
G_widget = widgets.FloatText(description='G:', value=300)
XN_widget = widgets.FloatText(description='XN:', value=20)
T_widget = widgets.FloatText(description='T:', value=250)
PMC_widget = widgets.FloatText(description='PMC:', value=0.8)
calcular_button = widgets.Button(description="Calcular")

# Función para calcular el GAP
def calcular(_):
    C0 = C0_widget.value
    C= C_widget.value
    PMC = PMC_widget.value
    T = T_widget.value
    I = I_widget.value
    G = G_widget.value
    XN = XN_widget.value
    Y = 1 / (1 - PMC) * (C0 - PMC * T + I + G + XN)
    Y2 = 1 / (1 - PMC) * (C - PMC * T + I + G + XN)
    GAP = (C0 - PMC * T + I + G + XN)
    GAP2 = (C - PMC * T + I + G + XN)
    PIB = round(GAP+PMC*Y, 2)
    PIB2 = round(GAP2+PMC*Y2, 2)
    print(f"GAP = {GAP} + ({PMC})Y")
    print(f"PIB = {PIB}\n") 
    print(f"GAP2 = {GAP2} + ({PMC})Y")
    print(f"PIB2 = {PIB2}")

    x = np.linspace(0, 10000, 100)

    y1 = x  # Línea 1: Pendiente 45°, pasa por (0, 0)
    y2 = GAP + PMC * x  # Línea 2: Pendiente = PMC, intersección en x=PIB
    y3 = GAP2 + PMC * x  # Línea 3: Pendiente = PMC, intersección en x=PIB

    # Graficar las líneas
    # Ajustar los límites del eje x e y
    plt.xlim(0, max(max(x), max(y1), max(y2)))
    plt.ylim(0, max(max(x), max(y1), max(y2)))  

    plt.plot(x, y1, 'r--', linewidth=2)  # Línea 1: Rojo, punteada
    plt.plot(x, y2, 'g-', linewidth=3)  # Línea 2: Verde, gruesa
    plt.plot(x, y3, 'g-', linewidth=3)  # Línea 3: Verde, gruesa
    plt.title('Avance en la gráfica determinación del equilibrio (Aspa Keynesiana o Cruz Keynesiana)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

    plt.show()

# Manejar los eventos de clic en el botón
calcular_button.on_click(calcular)

# Mostrar los widgets

display(C0_widget, I_widget, G_widget, XN_widget, T_widget, PMC_widget)
print("Si el consumo aumentó o disminuyó, ingrese el nuevo valor:")

display(C_widget,calcular_button)
