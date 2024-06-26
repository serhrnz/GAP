import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


# Definir los widgets para los parámetros
C0_widget = widgets.FloatText(description='C0:', value=620)
I_widget = widgets.FloatText(description='I:', value=220)
G_widget = widgets.FloatText(description='G:', value=300)
XN_widget = widgets.FloatText(description='XN:', value=20)
T_widget = widgets.FloatText(description='T:', value=250)
PMC_widget = widgets.FloatText(description='PMC:', value=0.8)

# Crear los botones
calcular_button = widgets.Button(description="Calcular")
calcular_button2 = widgets.Button(description="Calcular")

# Función para calcular el GAP
def calcular(_):
    global C0_widget2, I_widget2, G_widget2, XN_widget2, T_widget2, PMC_widget2
    C0 = C0_widget.value
    PMC = PMC_widget.value
    T = T_widget.value
    I = I_widget.value
    G = G_widget.value
    XN = XN_widget.value
    Y = 1 / (1 - PMC) * (C0 - PMC * T + I + G + XN)
    GAP = (C0 - PMC * T + I + G + XN)
    PIB = round(GAP+PMC*Y, 2)
    print(f"GAP = {GAP} + ({PMC})Y")
    print(f"PIB = {PIB}\n") 

    x = np.linspace(PIB*0.2, PIB*1.5, 100)

    y1 = x  # Línea 1: Pendiente 45°, pasa por (0, 0)
    y2 = GAP + PMC * x  # Línea 2: Pendiente = PMC, intersección en x=PIB

    # Graficar las líneas
    # Ajustar los límites del eje x e y

    # Crear una figura más grande
    plt.figure(figsize=(12, 8))

    plt.xlim(PIB*0.2, max(max(x), max(y1), max(y2)))
    plt.ylim(PIB*0.2, max(max(x), max(y1), max(y2)))  

    plt.plot(x, y1, 'r--', linewidth=2)  # Línea 1: Rojo, punteada
    plt.plot(x, y2, 'g-', linewidth=3)  # Línea 2: Verde, gruesa
    plt.title('Avance en la gráfica determinación del equilibrio (Aspa Keynesiana o Cruz Keynesiana)',pad=20)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: '{:,.0f}'.format(y)))

    ax.tick_params(axis='x', which='major', pad=10)  # Aumentar el espacio para el eje x
    ax.tick_params(axis='y', which='major', pad=10)  # Aumentar el espacio para el eje y

    ax.set_xlabel('PIB', labelpad=20)
    ax.set_ylabel('Gasto agregado planeado (GAP)', labelpad=20)

    plt.annotate('45°', xy=(x[-1], y1[-1]), xytext=(5, 0), textcoords='offset points', color='red')
    plt.annotate(f"GAP = {GAP} + ({PMC})Y", xy=(x[-1], y2[-1]), xytext=(5, 0), textcoords='offset points', color='green')
    
    # Trazar una línea punteada desde el punto (x_c, y_c) al eje y (x=0)
    plt.plot([PIB, PIB], [0, PIB], 'k--', label=f'{PIB}')  # Línea punteada vertical
    #plt.plot([0, PIB], [PIB, PIB], 'k--')  # Línea punteada horizontal

    # Marcar el punto c
    #plt.scatter([PIB], [PIB], color='red')  # Punto c en rojo
    plt.text(PIB, PIB*0.2, f'{PIB}', fontsize=12, verticalalignment='top',horizontalalignment='center')


    plt.show()


    print("Si alguna variable cambió, ingrese el nuevo valor:\n")

    C0_widget2 = widgets.FloatText(description='C0:',value=C0)
    I_widget2 = widgets.FloatText(description='I:',value=I)
    G_widget2 = widgets.FloatText(description='G:',value=G)
    XN_widget2 = widgets.FloatText(description='XN:',value=XN)
    T_widget2 = widgets.FloatText(description='T:',value=T)
    PMC_widget2 = widgets.FloatText(description='PMC:',value=PMC)
    display(C0_widget2, I_widget2, G_widget2, XN_widget2, T_widget2, PMC_widget2,calcular_button2)

def calcular2(_):
    C0 = C0_widget.value
    PMC = PMC_widget.value
    T = T_widget.value
    I = I_widget.value
    G = G_widget.value
    XN = XN_widget.value
    Y = 1 / (1 - PMC) * (C0 - PMC * T + I + G + XN)
    GAP = (C0 - PMC * T + I + G + XN)
    PIB = round(GAP+PMC*Y, 2)


    C02 = C0_widget2.value
    PMC2 = PMC_widget2.value
    T2 = T_widget2.value
    I2 = I_widget2.value
    G2 = G_widget2.value
    XN2 = XN_widget2.value
    Y2 = 1 / (1 - PMC2) * (C02 - PMC2 * T2 + I2 + G2 + XN2)
    GAP2 = (C02 - PMC2 * T2 + I2 + G2 + XN2)
    PIB2 = round(GAP2+PMC*Y2, 2)
    print(f"GAP = {GAP} + ({PMC})Y")
    print(f"PIB = {PIB}\n") 
    print(f"GAP2 = {GAP2} + ({PMC})Y")
    print(f"PIB2 = {PIB2}\n")

    zoom = max(0,max(PIB,PIB2)-(abs(PIB-PIB2)*2))
    limite = max(PIB,PIB2)+abs(PIB-PIB2)*.5
    x = np.linspace(zoom, limite, 100)

    y1 = x  # Línea 1: Pendiente 45°, pasa por (0, 0)
    y2 = GAP + PMC * x  # Línea 2: Pendiente = PMC, intersección en x=PIB
    y3 = GAP2 + PMC2 * x  # Línea 3: Pendiente = PMC, intersección en x=PIB2

    # Graficar las líneas
    # Ajustar los límites del eje x e y

    # Crear una figura más grande
    plt.figure(figsize=(12, 8))

    plt.xlim(zoom, limite)
    plt.ylim(zoom, limite)

    plt.plot(x, y1, 'r--', linewidth=2)  # Línea 1: Rojo, punteada
    plt.plot(x, y2, 'g-', linewidth=3)  # Línea 2: Verde, gruesa
    plt.plot(x, y3, 'g-', linewidth=3)  # Línea 3: Verde, gruesa
    plt.title('Avance en la gráfica determinación del equilibrio (Aspa Keynesiana o Cruz Keynesiana)',pad=20)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: '{:,.0f}'.format(y)))

    ax.tick_params(axis='x', which='major', pad=10)  # Aumentar el espacio para el eje x
    ax.tick_params(axis='y', which='major', pad=10)  # Aumentar el espacio para el eje y

    ax.set_xlabel('PIB', labelpad=20)
    ax.set_ylabel('Gasto agregado planeado (GAP)', labelpad=20)

    plt.annotate('45°', xy=(x[-1], y1[-1]), xytext=(5, 0), textcoords='offset points', color='red')
    plt.annotate(f"GAP = {GAP} + ({PMC})Y", xy=(x[-1], y2[-1]), xytext=(5, 0), textcoords='offset points', color='green',va='center')
    plt.annotate(f"GAP2 = {GAP2} + ({PMC2})Y", xy=(x[-1], y3[-1]), xytext=(5, 0), textcoords='offset points', color='green',va='center')

    # Trazar una línea punteada desde el punto (x_c, y_c) al eje y (x=0)
    plt.plot([PIB, PIB], [0, PIB], 'k--', label=f'{PIB}')  # Línea punteada vertical
    #plt.plot([0, PIB], [PIB, PIB], 'k--')  # Línea punteada horizontal

    # Marcar el punto c
    #plt.scatter([PIB], [PIB], color='red')  # Punto c en rojo
    if PIB>PIB2:
      plt.text(PIB, zoom, f'{PIB}', fontsize=12, verticalalignment='top',horizontalalignment='center')
    else:
      plt.text(PIB, zoom, f'{PIB}', fontsize=12, verticalalignment='top',horizontalalignment='center')

    # Trazar una línea punteada desde el punto (x_c, y_c) al eje y (x=0)
    plt.plot([PIB2, PIB2], [0, PIB2], 'k--', label=f'{PIB2}')  # Línea punteada vertical
    #plt.plot([0, PIB], [PIB, PIB], 'k--')  # Línea punteada horizontal

    # Marcar el punto c
    #plt.scatter([PIB], [PIB], color='red')  # Punto c en rojo
    if PIB>PIB2:
      plt.text(PIB2, zoom, f'{PIB2}', fontsize=12, verticalalignment='top',horizontalalignment='center')
    else:
      plt.text(PIB2, zoom, f'{PIB2}', fontsize=12, verticalalignment='top',horizontalalignment='center')

    plt.show()

    A = round((PIB-PIB2)*(1-PMC),2)

    if PIB>PIB2:
      print(f"El Gobierno debe aplicar una política fiscal expansiva, incrementando el gasto en {A} unidades para regresar al PIB de pleno empleo.")
    else:
      print(f"El Gobierno debe aplicar una política fiscal contractiva, disminuyendo el gasto en {-A} unidades para regresar al PIB de pleno empleo.")
    

# Manejar los eventos de clic en el botón
calcular_button.on_click(calcular)
calcular_button2.on_click(calcular2)

# Mostrar los widgets
print("\nIngrese los datos para el cálculo, donde: \nC0 = Consumo\nI = Inversión\nG = Gasto del Gobierno\nXN = Exportaciones Netas\nT = Impuestos\nPMC = Propensión marginal al consumo\n")
display(C0_widget, I_widget, G_widget, XN_widget, T_widget, PMC_widget,calcular_button)
