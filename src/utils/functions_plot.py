import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def dibujar_zipf_mesha(df, columna, colorin, titulo):
    '''
    Función que dibuja la representación de la ley de Zipf para textos

    df (pd.DataFrame): DataFrame con los datos que se quieren representar.
    columna (str): Columna del dataframe que se quiere analizar.
    colorin (str): Color que se quiere utilizar para el dibujo.
    titulo (str): Título de la gráfica.
    
    '''
    frecuencias = df[columna].value_counts()
    rangos = range(1, len(df[columna].value_counts())+1)
    m, k = np.polyfit(np.log10(rangos), np.log10(frecuencias), 1)
    plt.loglog(rangos, frecuencias, 'o', color = colorin)
    ajuste = (10**k)/(np.array(rangos))**(-1 * m)
    plt.loglog(rangos, ajuste, '--r')
    plt.xlabel('Rango')
    plt.ylabel('Frecuencia')
    plt.title(titulo)
    plt.show()
    # Después de dibujar, devuelve la pendiente de la recta ajustada por mínimos cuadrados
    return np.polyfit(np.log10(rangos), np.log10(frecuencias), 1)[0]

import numpy as np
def dibujar_zipf_at(df, columna, colorin, titulo):
    frecuencias = df[columna].sort_values(ascending=False)
    rangos = range(1,len(df[columna].sort_values())+1)
    m, k = np.polyfit(np.log10(rangos), np.log10(frecuencias), 1)
    plt.loglog(rangos, frecuencias, 'o', color =colorin)
    ajuste = (10**k)/(np.array(rangos))**(-1 * m)
    plt.loglog(rangos, ajuste, '--r')
    plt.xlabel('Posición del ranking')
    plt.ylabel('Frecuencia')
    plt.title(titulo)
    plt.show()
    # Después de dibujar, devuelve la pendiente de la recta ajustada por mínimos cuadrados
    return m