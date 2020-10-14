---
title: Línea de comandos
description: ""
weight: 2
---

Ahora te presentaré a uno de los mejores amigos del desarrollador: la línea de comandos.

Los siguientes pasos te mostrarán cómo usar aquella ventana negra que todos los hackers usan. Puede parecer mucha información al principio, pero piensa que solo es un mensaje en pantalla que espera a que le des órdenes.

## Línea de comandos

La ventana, que generalmente es llamada línea de comandos o interfaz de línea de comandos, es una aplicación basada en texto para ver, manejar y manipular archivos en tu computadora. Tiene una función similar al Explorador de Windows o Finder en Mac, pero sin la interfaz gráfica. Otros nombres para la línea de comandos son: _cmd_, _CLI_, _prompt_, _símbolo del sistema_, _consola_ o _terminal_.

### Abrir la interfaz

Lo primero que debemos hacer para empezar a experimentar con nuestra interfaz de línea de comandos es abrirla.

Dependiendo de tu sistema operativo y tu teclado, podrías encontrarla en diferentes partes (tendrás que experimentar un poco, hasta que alguna de estas sugerencias funcione):

-   Ve al menú o pantalla de Inicio, y escribe "Símbolo del Sistema" o "Command Prompt" en el cuadro de búsqueda.
-   Ve a `Menú de inicio → Sistema de Windows → Simbolo del sistema` (`Start menu → Windows System → Command Prompt`).
-   Ve a `Menú de Inicio → Todos los Programas → Accessorios → Símbolo del Sistema` (`Start menu → All Programs → Accessories → Command Prompt`).
-   Ve a la pantalla de Inicio, pasa el ratón sobre la esquina inferior izquierda de la pantalla, y haz click en la flecha hacia abajo. La página de la Aplicaciones debería abrirse. Haz click en Símbolo del Sistema en la sección Sistema de Windows.
-   Mantén pulsada la tecla especial de Windows de tu teclado y pulsa "X". Elige `Símbolo del Sistema` (`Command Prompt`) del menú emergente.
-   Mantén pulsada la tecla especial de Windows y pulsa "R" para abrir la ventana `Ejecutar` (`Run`). Escribe `cmd` en la caja, y haz click en OK.

Si estas utilizando Linux está probablemente en `Aplicaciones → Accesorios → Terminal` o `Aplicaciones → Sistema → Terminal`, pero todo depende de la distribución de Linux que utilices. Si no se encuentra en ninguno de estos sitios, puedes usar el buscador de Google.

### Prompt

Ahora deberías ver una ventana blanca o negra que está esperando tus órdenes. Depende el sistema operativo ya sea `cmd` en Windows o `bash` (que incluye a _Git Bash_, _Linux_, y _Mac OS X_, a menos que se indique lo contrario), puedes ver diferentes textos.

{{< tabs >}}
{{< tab "bash" >}}

```sh
$
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
>
```

{{< /tab >}}
{{< /tabs >}}

Este segundo prompt es el que se verá cuando utilicemos _PythonAnywhere_ más adelante.

Cada comando será precedido por alguno de estos signos `$` o `>` y un espacio, así que no tienes que escribirlo - tu consola lo hará por ti.

{{%notice info%}}
**Nota:** Dependiendo el caso tu consola podrías estar viendo algo como `C:\Users\carlos` o `Carlos-MacBook-Pro:~ carlos$` antes del símbolo de prompt, esto es porque dependiendo la consola te puede dar mas información como en que directorio estas, la ruta completa, o el usuario actual.
{{%/notice%}}

La parte hasta e incluyendo el `$` o `>` es llamada _promp de linea de comandos_ o _prompt_ para abreviar. Te _sugiere_ (prompt en ingles) para que des una entrada allí.

En futuras prácticas, cuando se requiera que escribas algún comando, si se incluye `$` o `>`, y ocasionalmente algo más a la izquierda del símbolo. Ignora toda esta parte izquierda y solo escribe el comando, que inicia justo despues del prompt.

### Primer comando

En este tutorial, para homologar casos de usos, estaremos utilizando _Git Bash_ que viene por defecto con _Git_ (denotado como `bash` cuando se vayan a ejecutar comandos). Ya que está consola se ejecuta y ve igual en todos los sistemas operativos; nos facilita hablar a todos el mismo idioma.

{{%notice primary%}}
Si algo no funciona en _Git Bash_ utiliza la consola por defecto de tu sistema operativo.
{{%/notice%}}

Vamos a empezar con algo simple. Escribe este comando:

{{< tabs >}}
{{< tab "bash" >}}

```sh
whoami
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
whoami
```

{{< /tab >}}
{{< /tabs >}}

Y luego oprime la tecla Enter. Este es el resultado:

{{< tabs >}}
{{< tab "bash" >}}

```sh
carlos
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
ubx-carlos\carlos
```

{{< /tab >}}
{{< /tabs >}}

Como puedes ver, la computadora sólo presentá tu nombre de usuario.

{{%notice info%}}
**Nota:** Como puedes ver en mi caso para Windows aparece el hostname (nombre de la máquina) `ubx-carlos` y el usuario `carlos`. Esto es correcto y algunas consolas podría mostrar lo mismo de manera diferente, por ejemplo separandolos con `@` (`ubx-carlos@carlos`).
{{%/notice%}}

{{%notice primary%}}
Trata de escribir cada comando, no copies y pegues. Te será de mejor práctica para recordarlos en el futuro.
{{%/notice%}}

## Comandos básicos

Cada sistema operativo tiene un conjunto ligeramente diferente de comandos para la línea de comandos, así que asegúrate de seguir las instrucciones para tu sistema operativo.

### Directorio actual

Sería bueno saber dónde nos encontramos en este momento dentro de la estructura de directorios. Escribe este comando y oprime `Enter`:

{{< tabs >}}
{{< tab "bash" >}}

```sh
pwd
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
cd
```

{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
**Nota:** `pwd` significa _Print Working Directory_ (en español, _mostrar directorio de trabajo_). `cd` significa _Current Directory_ (en español, _directorio actual_).
{{%/notice%}}

El resultado

{{< tabs >}}
{{< tab "bash" >}}

```sh
/c/Users/carlos
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
C:\Users\carlos
```

{{< /tab >}}
{{< /tabs >}}

Probablemente verás algo similar en tu máquina. Una vez que abres la línea de comandos generalmente empiezas en el directorio base de tu perfil de usuario.

### Como aprender más sobre un comando

Muchos comandos que puedes introducir a la linea de comando tienen integrada una ayuda que puedes desplegar y leer. Por ejemplo, para aprender más sobre el comando de directorio actual.

En Windows, puedes agregar un `/?` como sufijo a la mayoria de comandos y se imprimirá en pantalla la página de ayuda. Puede que necesites deslizar hacia abajo tu ventana para ver toda la ayuda. Intenta con `cd /?`.

En Linux, tienen el comando `man`, que te muestra la ayuda o manual de los comandos. Intenta `man pwd` y mira lo que dice, o escribe `man` antes de otros comandos para ver la ayuda. La salida del comando `man` se encuentra paginada, así que usa la barra de espacio para moverte a la siguiente pagina, y `q` para salir de la ayuda.

En Git Bash no hay un comando genérico para ver la ayuda de los comandos, pero muchos comandos tienen un parametro para mostrar la ayuda, puedes intentar con `pwd --help` o algunas veces `-h`.

### Listar archivos y directorios

Siempre es bueno poder listar los archivos que hay en el directorio actual. Para hacer esto podemos usar el siguiente comando.

{{< tabs >}}
{{< tab "bash" >}}

```sh
$ ls
Applications
Desktop
Downloads
Music
...
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
> dir
Volume in drive C is Windows
 Volume Serial Number is D611-43D1

 Directory of C:\Users\carlos

10/03/2019  04:54 PM    <DIR>          Desktop
09/27/2019  09:01 AM    <DIR>          Documents
10/04/2019  10:52 AM    <DIR>          Downloads
```

{{< /tab >}}
{{< /tabs >}}

### Cambiar de directorio

Vamos ahora a nuestro directorio de Escritorio (Desktop).

{{< tabs >}}
{{< tab "bash" >}}

```sh
cd Desktop
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
cd Desktop
```

{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
**Nota:** Toma en cuenta que el directorio _Desktop_ puede tener un nombre traducido al lenguaje de tu sistema operativo. Si ese es el caso, tendras que remplazar _Desktop_ por el nombre traducido; por ejemplo, _Escritorio_ en Español.
{{%/notice%}}

Comprueba si realmente ha cambiado. En Linux y OS X:

{{< tabs >}}
{{< tab "bash" >}}

```sh
$ pwd
/c/Users/carlos/Desktop
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
> cd
C:\Users\carlos\Desktop
```

{{< /tab >}}
{{< /tabs >}}

{{%notice tip%}}
**Tip**
\
Si escribes `cd D` y luego oprimes **TAB** en el teclado, la línea de comandos automáticamente completará el resto del nombre para que puedas navegar más rápido. Si hay más de una carpeta que empiece con `D`, presiona la tecla **TAB** dos veces para obtener una lista de opciones.
{{%/notice%}}

### Crear directorios

¿Qué tal si creamos un directorio para practicar en tu escritorio? Puedes hacerlo de esta manera:

{{< tabs >}}
{{< tab "bash" >}}

```sh
mkdir practica
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
mkdir practica
```

{{< /tab >}}
{{< /tabs >}}

Este pequeño comando creará una carpeta con el nombre `practica` en tu escritorio. Puedes comprobar si está allí buscando en tu escritorio utilizando el explorador de archivos o ejecutando el comando `ls`/`dir`.

{{%notice tip%}}
**Tip**
\
Si no quieres escribir una y otra vez los mismos comandos, prueba oprimiendo la flecha arriba y flecha abajo de tu teclado para ver los comandos utilizados de manera reciente.
{{%/notice%}}

## Ejercicios

Un pequeño reto para ti: en el directorio recién creado `practica` crea un directorio llamado `test`. Utiliza los comandos `cd` y `mkdir`.

{{< tabs >}}
{{< tab "bash" >}}

```sh
$ cd practica
$ mkdir test
$ ls
test
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
> cd practica
> mkdir test
> dir
05/08/2019 07:28 PM <DIR>      test
```

{{< /tab >}}
{{< /tabs >}}

## Limpiar

No queremos dejar un desorden, así que vamos a eliminar todo lo que hicimos hasta este momento. En primer lugar, tenemos que volver al directorio _Desktop_:

{{< tabs >}}
{{< tab "bash" >}}

```sh
$ cd ..
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
> cd ..
```

{{< /tab >}}
{{< /tabs >}}

Usando `..` en el comando `cd` cambiará el directorio actual al directorio padre (que es el directorio que contiene el directorio actual).

{{< tabs >}}
{{< tab "bash" >}}

```sh
$ pwd
/c/Users/carlos/Desktop
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
> cd
C:\Users\carlos\Desktop
```

{{< /tab >}}
{{< /tabs >}}

Es hora de eliminar el directorio `practica`.

{{%notice warning%}}
**Precaución**
\
Eliminar archivos utilizando `del`, `rmdir` o `rm` hace que no puedan recuperarse, lo que significa que los archivos borrados **desaparecerán para siempre**, debes ser muy cuidadoso con estos comandos.
{{%/notice%}}

{{< tabs >}}
{{< tab "bash" >}}

```sh
rm -r practica
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
> rmdir /S practica
practica, Are you sure <Y/N>? Y
```

{{< /tab >}}
{{< /tabs >}}

Hecho, asegurémonos que en verdad fue borrado.
{{< tabs >}}
{{< tab "bash" >}}

```sh
ls
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
dir
```

{{< /tab >}}
{{< /tabs >}}

## Salir

Ahora puedes cerrar la línea de comandos sin problemas. Vamos a hacerlo al estilo hacker:

{{< tabs >}}
{{< tab "bash" >}}

```sh
exit
```

{{< /tab >}}
{{< tab "cmd" >}}

```bat
exit
```

{{< /tab >}}
{{< /tabs >}}

## Resumen

Aquí hay una lista resumen de algunos comandos útiles:

| Comando (Windows) | Comando (Bash / Linux) | Descripción                      | Ejemplo                                             |
| ----------------- | ---------------------- | -------------------------------- | --------------------------------------------------- |
| `exit`            | `exit`                 | Cierra la ventana                | **`exit`**                                          |
| `cd <path>`       | `cd`                   | Cambia el directorio             | **`cd test`**                                       |
| `cd`              | `pwd`                  | Muestra la ruta actual           | **`cd`** (Windows) o **`pwd`** (OS X / Linux)       |
| `dir`             | `ls`                   | Lista archivos/directorios       | **`dir`**                                           |
| `copy`            | `cp`                   | Copia de archivos                | **`copy c:\test\text.txt c:\windows\test.txt`**     |
| `move`            | `mv`                   | Mueve archivos                   | **`move c:\test\text.txt c:\windows\test.txt`**     |
| `mkdir`           | `mkdir`                | Crea un directorio nuevo         | **`mkdir testdirectory`**                           |
| `rmdir` (o `del`) | `rm`                   | Elimina archivos                 | **`del c:\test\test.txt`**                          |
| `rmdir /S`        | `rm -r`                | Elimina directorios              | **`rm -r testdirectory`**                           |
| `[CMD] /?`        | `man [CMD]`            | Muestra la ayuda de los comandos | **`cd /?`** (Windows) o **`man cd`** (OS X / Linux) |

Estos son solo algunos de los comandos que puedes ejecutar en la línea de comandos. No vas a usar nada más que esos por ahora.

Si tienes curiosidad, [ss64.com](http://ss64.com/) contiene una referencia completa de comandos para todos los sistemas operativos.
