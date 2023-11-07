 # Bibliotecas necesarias
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt
from .functions_text import *

def importar_palabras_biblia():
    '''Función que importa dataset de la obra de Strong, con todas las palabras del Antiguo Testamento'''
    try:
        a = pd.read_excel('https://query.data.world/s/3ljivu4i6mi4qbhw3plofrb4nztdkg?dws=00000')
        # No se devuelven las ocurrencias de raíces en palabras compuestas ya que no aporta nada al análisis
        biblia = a.loc[:,:'word_root_occurrence'].copy()
        biblia['transcripcion'] = biblia['root_word'].apply(feniciohebreo_a_latino)
        return biblia
    except:
        print('Imposible importar el dataset de la Biblia')
        return 0
    

def importar_mesa():
    # Webscraping del texto de la estela de Mesa expuesto en el artículo de Wikipedia
    enlace ='https://en.wikipedia.org/wiki/Mesha_Stele'
    respuesta = requests.get(enlace)
    try:
        soup = bs(respuesta.content, 'html.parser')
        texto_por_linea = soup.find_all('span', class_="script-phoenician")
        mesa = pd.DataFrame({'Texto':[i.get_text() for i in texto_por_linea]})
        # Columna del número de línea en la estela
        mesa['línea'] = mesa.index+1
        return mesa
    except:
        # Si hay un error en la conexión, muestra el error
        print('Error en la conexión')
        print(respuesta)
        return 0

def palabras_mesa(df_lineas):
    '''
    df_lineas (pd.DataFrame): Requiere un dataframe de pandas con el texto de la estela por líneas.

    Función que devuelve un dataset con el texto por palabras. Corrige irregularidades en la primera línea.
    '''
    # Hay un error en la primera línea que voy a corregir a mano:
    palabras = df_lineas.loc[0,'Texto'].split()  
    palabras.pop(7)
    palabras.pop(7)

    linea_1 = [i for i in palabras if i != '𐤟']
    # Generacion del dataframe de palabras:
    diccionario_mesa = {'palabra':[], 'linea_estela':[], 'numero_oracion':[]}
    #línea 1:
    numero_oracion = 1
    for i in linea_1:
        diccionario_mesa['palabra'].append(i)
        diccionario_mesa['linea_estela'].append(1)
        diccionario_mesa['numero_oracion'].append(numero_oracion)

    # Resto de estela:
    for fila in range(1, len(df_lineas)-1):
        linea = [i for i in df_lineas.loc[fila, 'Texto'].split() if i != '𐤟']
        for  num, palabra in enumerate(linea):
            palabra = palabra.replace('[', '')
            palabra = palabra.replace(']', '')
            palabra = palabra.replace('.', '')
            palabra = palabra.replace('𐤟', '')
            # Unir primera palabra de la línea a la palabra anterior salvo en las líneas 19, 25 y 26
            if (fila not in [19, 25, 26]) and num == 0:
                diccionario_mesa['palabra'][-1] = diccionario_mesa['palabra'][-1] + palabra
            else:

                if palabra == '|':
                    numero_oracion += 1
                else:
                    
                    diccionario_mesa['palabra'].append(palabra)
                    diccionario_mesa['linea_estela'].append(fila+1)
                    diccionario_mesa['numero_oracion'].append(numero_oracion) 

    a = pd.DataFrame(diccionario_mesa)
    # Unir final de línea con inicio de línea. Voy a hacerlo hasta la línea 26, después ya está perdido el comienzo de línea
    a['transcripcion'] = a['palabra'].apply(feniciohebreo_a_latino)
    return a


def letras_mesa(df_palabras):
    cadena_letras = ''
    for i in range(len(df_palabras)):
        cadena_letras += df_palabras.loc[i, 'palabra']
    a = pd.DataFrame({'letra':[i for i in cadena_letras]})
    a['transcripcion'] = a['letra'].apply(feniciohebreo_a_latino)
    return a

def conteo_letras_at(biblia):
    '''biblia (pd.DataFrame): DataFrame de palabras del Antiguo Testamento de Strong
    Devuelve un dataframe con una lista de letras de la Biblia.
    '''
    cadena_letras = ''
    for i in range(len(biblia)):
        # Suma la palabra el número de veces que aparece en la Biblia
        for j in range(biblia.loc[i, 'occurrences'] - 1):
            cadena_letras += biblia.loc[i, 'word']

    lista_letras = []
    # Crea una lista con todas las letras del AT
    for i in cadena_letras:
        if i in 'אבגדהוזחטיכךלמםנןסעפףצץקרשת':
            # Se cambian grafías finales por las centrales para que la letra final no se contabilice como letra distinta
            if i == 'ך':
                letra = 'כ'
            elif i == 'ם':
                letra = 'מ'
            elif i == 'ן':
                letra = 'נ'
            elif i == 'ף':
                letra = 'פ'
            elif i == 'ץ':
                letra = 'צ'
            else:
                letra = i
            lista_letras.append(letra)
    a = pd.DataFrame({'letra_hebrea':lista_letras})
    a['transcripcion'] = a['letra_hebrea'].apply(feniciohebreo_a_latino)
    return a