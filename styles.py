def load_stylesheet():
    '''

    :return: boolean
    Carga y devuelve el contenido del stylesheet como una cadena

    '''
    with open('styles.qss', 'r') as style_file:
        return style_file.read()