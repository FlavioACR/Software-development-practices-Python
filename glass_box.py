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

