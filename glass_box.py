"""Estas pruebas se basan en el flujo del programa.
Asumen que el desarrollador conoce la implementación.

Son muy recomendadas cuanto se tiene que hacer un 
Regression Testing o Mocks (Cuando se tiene un bug con el 
programa ya salio a luz).

Prueba todos los caminos de una función;
Ramificacionez, bucles for y while, recursiones.
* Cuando se tiene un if:
    * Se recomienda probar todas la condiciones; if, elif, else.
* Cuando se tiene un 'for' loop:
    * Se recomienda probar un test en cada una de la opciones:
        * Sin entrar loop
        * Entrando una vez
        * Entrando mas de una vez
* Cuando se tiene un while loop:
    * Se recomienda hacer una pruba en los siguientes escenarios:
        * La condicion de entrada es falsa(False)
        * La condicion de entrada en verdadera(True)

Es importante probar todas la excepcione del codigo, es decir donde el
flujo pueda ser truncado"""

import unittest

def es_mayor_de_edad(edad):
    '''Esta función comprueba la mayoria de edad
    del parametro edad como entrada
    
    Para hacer el testing es necesario recorrer
    todas sus posibilidades en este caso solo son dos
    if, else, True y False. Por lo cual se tendra
    que hacer un testing por cada uno.
    '''
    if edad >= 18:
        return True
    else:
        return False
    


class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20
        # Se aplica la funcion o codigo para el testing:
        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15
        # Se aplica la funcion o codigo para el testing:
        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)



if __name__ == '__main__':
    unittest.main()

