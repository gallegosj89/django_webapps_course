---
title: Challenge
weight: 10
---

Como seguramente hicieron desde el principio del curso han seguido un tutorial de Python en linea, ya saben los tipos de datos que existe, estan familiarizados con la sintaxis. En otras palabras ya pasaron de un nivel basico a un nivel intermedio de experiencia en Python. Ademas cuentan con los años de programación que han acumulado a lo largo de su carrera.

En este ejercicio, para poner a prueba sus habilidades, se construirá un script para jugar el juego del _Ahorcado_. En el juego del _Ahorcado_, el jugador solo puede tener 6 respuestas incorrectas (cabeza, cuerpo, 2 piernas, y 2 brazos) antes de que pierda el juego, el objetivo es adivinar una palabra seleccionada al azar.

Los pasos que debe de cumplir este script son:

1. Seguir las reglas del juego.
2. Cargar una palabra de forma aleatoria desde el diccionario [`lemario.txt`](https://drive.google.com/file/d/1G-p_BsJp_urh2a6wDhnuvw3_ovIHqDTb/view?usp=sharing).
3. Crear la lógica para adivinar la palabra y presentar esta información al usuario en todo momento.
4. Mantener el seguimiento de las letras adivinadas por el usuario y sus errores, es decir, si el usuario adivina con una letra antes usada no se debe penalizar.
5. Cuando el usuario gane o pierda, dejar que decida si quiere jugar de nuevo.
6. En lugar de mostrarle al usuario "Tienes 4 respuestas incorrectas restantes.", mostrar una imagen o representación del "Ahorcado". (Esto es un reto adicional, realizar primero la lógica del juego.)

> Pistas: entrada del teclado, manejo de archivos (with/open), encoding, generador de número aleatorio, listas (elemento _in_ lista), sets, convertir todo a mayusculas/minusculas. La solución será mucho mas limpia si se utilizan funciones.
