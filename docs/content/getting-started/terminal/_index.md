---
title: Línea de comandos
description: ""
weight: 2
---

# Introducción a la interfaz de línea de comandos

Permíteme presentarte a tu primer nuevo amigo: ¡la línea de comandos!

Los siguientes pasos te mostrarán cómo usar aquella ventana negra que todos los hackers usan. Puede parecer un poco aterrador al principio pero es solo un mensaje en pantalla que espera a que le des órdenes.

## Línea de comandos

La ventana, que generalmente es llamada línea de comandos o interfaz de línea de comandos, es una aplicación basada en texto para ver, manejar y manipular archivos en tu computadora. Tiene una función similar al Explorador de Windows o Finder en Mac, pero sin la interfaz gráfica. Otros nombres para la línea de comandos son: _cmd_, _CLI_, _prompt_, _símbolo del sistema_, _consola_ o _terminal_.

## Abrir la interfaz de línea de comandos

Lo primero que debemos hacer para empezar a experimentar con nuestra interfaz de línea de comandos es abrirla.

Dependiendo de tu version de Windows y tu teclado, podrias encontrarla en diferencetes partes (tendras que experimentar un poco, pero no tendras que probar todas estas sugerencias):

-   Ve al menú o pantalla de Inicio, y escribe "Símbolo del Sistema" o "Command Prompt" en el cuadro de búsqueda.
-   Ve a Menú de inicio → Sistema de Windows → Simbolo del sistema (Start menu → Windows System → Command Prompt).
-   Ve al menú de Inicio → Todos los Programas → Accessorios → Símbolo del Sistema (Start menu → All Programs → Accessories → Command Prompt).
-   Ve a la pantalla de Inicio, pasa el ratón sobre la esquina inferior izquierda de la pantalla, y haz click en la flecha hacia abajo. La página de la Aplicaciones debería abrirse. Haz click en Símbolo del Sistema en la sección Sistema de Windows.
-   Mantén pulsada la tecla especial de Windows de tu teclado y pulsa "X". Elige _Símbolo del Sistema_ (Command Prompt) del menú emergente.
-   Mantén pulsada la tecla especial de Windows y pulsa "R" para abrir la ventana _Ejecutar_ (Run). Escribe _cmd_ en la caja, y haz click en OK.

Si estas utilizando Linux está probablemente en Aplicaciones → Accesorios → Terminal o Aplicaciones → Sistema → Terminal, pero todo depende de la distribución de Linux que utilices. Si no se encuentra en ninguno de estos sitios, puedes usar el buscador de Google.

### Prompt

Ahora deberías ver una ventana blanca o negra que está esperando tus órdenes.

En Linux o OS X verás algo como esto:

```bash
$
```

En Windows, probablemente verás:

```bash
C:\Users\Name>
```

Este segundo prompt es el que se verá cuando utilizemos _PythonAnywhere_ mas adelante.

Cada comando será precedido por alguno de estos signos `$` o `>` y un espacio, así que no tienes que escribirlo - tu computadora lo hará por ti.

> Una pequeña nota: en tu caso podria estar algo como `C:\Users\carlos` o `Carlos-MacBook-Pro:~ carlos$` antes del simbolo de prompt, esto es 100% correcto.

La parte hasta e incluyendo el `$` o `>` es llamada _promp de linea de comandos_ o _prompt_ para abreviar. Te _sugiere_ (prompt en ingles) para que des una entrada allí.

En futuras prácticas, cuando se requiera que escribas algun comando, si incluira `$` o `>`, y ocacionalmente algo mas a la izquierda. Ignora toda esta parte izquierda y solo escribe el comando, que inicia justo despues del prompt.

### Primer comando

Vamos a empezar con algo simple. Escribe este comando:

```bash
> whoami
```

Y luego oprime la tecla Enter. Este es el resultado:

```bash
> whoami
carlos
```

Como puedes ver, la computadora sólo presentá tu nombre de usuario.

> Trata de exribir cada comando, no copies y pegues. Recordaras más de esta manera.

## Comandos básicos

Cada sistema operativo tiene un conjunto ligeramente diferente de comandos para la línea de comandos, así que asegúrate de seguir las instrucciones para tu sistema operativo.

### Directorio actual

Sería bueno saber dónde nos encontramos en este momento dentro de la estructura de directorios. Escribe este comando y oprime `Enter`:

En Linux y OS X:

```bash
$ pwm
/home/carlos
```

En Wndows:

```bash
> cd
C:\Users\carlos
```

> Nota: '`pwd`' significa 'print working directory' - en español, 'mostrar directorio de trabajo'. `cd` significa 'change directory' - en español, 'cambiar directorio'.

Probablemente verás algo similar en tu máquina. Una vez que abres la línea de comandos generalmente empiezas en el directorio base de tu perfil de usuario.

### Como aparender más sobre un comando

Muchos comandos que puedes introducir a la linea de comando tienen integrada una ayuda que puedes desplegar y leer. Por ejemplo, para aprende mas sobre el comando de directorio actual.

En Windows, puedes agegar un `/?` como sufijo a la mayoria de comandos y se imprimira en pantalla la página de ayuda. Puede que necesites hcer scroll a tu ventana para verla toda. Intenta con `cd /?`.

En Linux y OS X, tienen el comando `man`, que te muestra la ayuda o manual de los comandos. Intenta `man pwd` y mira lo que dice, o pon `man` antes de otros comandos para ver la ayuda. La salida del comando `man` se encuentra paginada, así que usa la barra de espacio para moverte a la siguiente pagina, y `q` para salir de la ayuda.

Algunos comandos tambien tienen un parametro para mostrar la ayuda, puede intentar tambien `pwm --help` o algunas veces `-h`.

### Listar archivos y directorios

Siempre es bueno saber que se encuentra en el directorio actual. PAra eso podmeos usar el sigueinte comando:

En Linux y OS X:

```bash
$ ls
Applications
Desktop
Downloads
Music
...
```

En Windows:

```bash
$ dir
Volume in drive C is Windows
 Volume Serial Number is D611-43D1

 Directory of C:\Users\carlos

10/03/2019  04:54 PM    <DIR>          Desktop
09/27/2019  09:01 AM    <DIR>          Documents
10/04/2019  10:52 AM    <DIR>          Downloads
...
```

> Nota: En algunas terminales en Windows es posible usar `ls` como en Linux y Mac OS X.

### Cambiar de directorio

Vamos ahora a nuestro directorio de Escritorio (Desktop).

```bash
> cd Desktop
```

> Toma en cuenta que el directorio _Desktop_ puede tener un nombre traducido al lenguaje de tu sistema operativo. Si ese es el caso, tendras que remplazar `Desktop` por el nombre traducido; por ejemplo, `Escritorio` en Español.

Comprueba si realmente ha cambiado. En Linux y OS X:

```bash
$ pwd
/home/carlos/Desktop
```

En Windows:

```bash
> cd
C:\Users\carlos\Desktop
```

> Pro tip: si escribes `cd D` y luego oprimes **TAB** en el teclado, la línea de comandos automáticamente completará el resto del nombre para que puedas navegar más rápido. Si hay más de una carpeta que empiece con `D`, presiona el botón **TAB** dos veces para obtener una lista de opciones.

### Crear directorios

¿Qué tal si creamos un directorio de practica en tu escritorio? Puedes hacerlo de esta manera:

```bash
mkdir practica
```

Este pequeño comando creará una carpeta con el nombre `practica` en tu escritorio. Puedes comprobar si está allí buscando en tu escritorio o ejecutando el comando `ls`.

> Pro tip: Si no quieres escribir una y otra vez los mismos comandos, prueba oprimiendo la flecha arriba y flecha abajo de tu teclado para ver los comandos utilizados de manera reciente.

## Ejercicios

Un pequeño reto para ti: en el directorio recién creado `practica` crea un directorio llamado `test`. Utiliza los comandos `cd` y `mkdir`.

Solución en Linux y OS X:

```bash
$ cd practica
$ mkdir test
$ ls
test
```

Solución en Windows:

```bash
> cd practica
> mkdir test
> dir
05/08/2019 07:28 PM <DIR>      test
```

## Limpiar

No queremos dejar un desorden, así que vamos a eliminar todo lo que hicimos hasta este momento. En primer lugar, tenemos que volver al directorio _Desktop_:

```bash
cd ..
```

Usando `..` en el comando `cd` cambiará el directorio actual al directorio padre (que es el directorio que contiene el directorio actual).

Revisa dónde estás, Linux y OS X:

```bash
$ pwd
/home/carlos/Desktop
```

En Windows:

```bash
> cd
C:\Users\carlos\Desktop
```

Es hora de eliminar el directorio `practica`.

> Atención: Eliminar archivos utilizando `del`, `rmdir` o `rm` hace que no puedan recuperarse, lo que significa que los _archivos borrados desaparecerán para siempre_! debes ser muy cuidadoso con estos comandos.

En Linux y OS X:

```bash
rm -r practica
```

En Windows:

```bash
> rmdir /S practica
practica, Are you sure <Y/N>? Y
```

Hecho! Asegurémonos que en verdad fue borrado, en Linux y OS X:

```bash
ls
```

En Windows:

```bash
dir
```

## Salir

Ahora puedes cerrar la línea de comandos sin problemas. Vamos a hacerlo al estilo hacker:

```bash
exit
```

## Resumen

Aquí hay una lista resumen de algunos comandos útiles:

| Comando (Windows) | Comando (Linux / OS X) | Descripción                      | Ejemplo                                             |
| ----------------- | ---------------------- | -------------------------------- | --------------------------------------------------- |
| `exit`            | `exit`                 | Cierra la ventana                | **`exit`**                                          |
| `cd`              | `cd`                   | Cambia el directorio             | **`cd test`**                                       |
| `cd`              | `pwd`                  | Muestra la ruta actual           | **`cd`** (Windows) o **`pwd`** (OS X / Linux)       |
| `dir`             | `ls`                   | Lista archivos/directorios       | **`dir`**                                           |
| `copy`            | `cp`                   | Copia de archivos                | **`copy c:\test\text.txt c:\windows\test.txt`**     |
| `move`            | `mv`                   | Mueve archivos                   | **`move c:\test\text.txt c:\windows\test.txt`**     |
| `mkdir`           | `mkdir`                | Crea un directorio nuevo         | **`mkdir testdirectory`**                           |
| `rmdir (or del)`  | `rm`                   | Elimina archivos                 | **`del c:\test\test.txt`**                          |
| `rmdir /S`        | `rm -r`                | Elimina directorios              | **`rm -r testdirectory`**                           |
| `[CMD] /?`        | `man [CMD]`            | Muestra la ayuda de los comandos | **`cd /?`** (Windows) o **`man cd`** (OS X / Linux) |

Estos son solo algunos de los comandos que puedes ejecutar en la línea de comandos. No vas a usar nada más que esos por ahora.

Si tienes curiosidad, [ss64.com](http://ss64.com/) contiene una referencia completa de comandos para todos los sistemas operativos.
