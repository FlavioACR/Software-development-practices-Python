'''Afirmaciones: Verifican que las inputs sean lo que se esperaba.

* Programación defensiva
* Pueden utilizarse para verificar que los tipos sean correctos en una función
* También sirven para debuguear
'''
# Forma de las afirmaciones:
# assert <expresion booleana>. <mensaje de error>
# Ejemplo de assert(afirmación)

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras

