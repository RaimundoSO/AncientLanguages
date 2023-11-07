

def feniciohebreo_a_latino(palabra):
    '''
    palabra (str): palabra en alfabeto fenicio o hebreo que se quiere trasliterar
    Esta función traslitera a alfabeto latino cualquier palabra escrita en fenicio o hebreo.
    '''
    try:
        string = []
        for i in palabra:
            if i == '𐤀' or i == 'א':
                string.append('A')
            elif i == '𐤁' or i == 'ב':
                string.append('b')
            elif i == '𐤂' or i == 'ג':
                string.append('g')
            elif i == '𐤃' or i == 'ד':
                string.append('d')
            elif i == '𐤄' or i == 'ה':
                string.append('h')
            elif i == '𐤅' or i == 'ו':
                string.append('w')
            elif i == '𐤆' or i == 'ז':
                string.append('z')
            elif i == '𐤇' or i == 'ח':
                string.append('H')
            elif i == '𐤈' or i == 'ט':
                string.append('T')
            elif i == '𐤉' or i == 'י':
                string.append('y')
            elif i == '𐤊' or i == 'ך' or i == 'כ':
                string.append('k')
            elif i == '𐤋' or i == 'ל':
                string.append('l')
            elif i == '𐤌' or i == 'ם' or i == 'מ':
                string.append('m')
            elif i == '𐤍' or i == 'ן' or i == 'נ':
                string.append('n')
            elif i == '𐤎' or i == 'ס':
                string.append('s')
            elif i == '𐤏' or i == 'ע':
                string.append('3')
            elif i == '𐤐' or i == 'ף' or i == 'פ':
                string.append('p')
            elif i == '𐤑' or i == 'ץ' or i == 'צ':
                string.append('S')
            elif i == '𐤒' or i == 'ק':
                string.append('q')
            elif i == '𐤓' or i == 'ר':
                string.append('r')
            elif i == '𐤔' or i == 'ש':
                string.append('š')
            elif i == '𐤕' or i == 'ת':
                string.append('t')
            else:
                print('Caracter no reconocido')
                return 0
        return ''.join(string)
    except:
        print('Caracter no iterable')
        return 0
    

def diccionario(df_hebreo, df_mesha):
    traduccion = []
    print('Bienvenido al traductor por líneas de la estela de Mesha.')
    linea = int(input('Introduce la línea que quieres traducir: '))
    for i in df_mesha[df_mesha['numero_oracion'] == linea].loc[:,'transcripcion']:
        print('Posibles traducciones para', i)
        print(df_hebreo[df_hebreo['transcripcion'] == i]['gloss'])
        a = input('¿Cuál te parece mejor? ')
        if a == '':
            traduccion.append(i)
        else:
            traduccion.append(a)
    return ' '.join(traduccion)

