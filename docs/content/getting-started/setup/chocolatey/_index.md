---
title: Chocolatey
weight: 5
---

Chocolatey (`choco`) es una administrador de paquetes para _Windows_ similar a lo que es `apt` en _Ubuntu_, `pacman` en _Arch_, o `yum` en _Fedora_.

En general podemos utilizar `choco` para instalar todas las dependencias de este tutorial, pero siempre es mejor aprende a instalarlas por uno mismo. Aquí lo vamos a utilizar para instalar algunas utilizades que no tienen un instalador disponible y que solo pueden ser instaladas por medio de `choco`.

{{%notice info%}}
Para una guía siempre actualizada en ingles, ve a la [página oficial de instalación](https://chocolatey.org/install).
{{%/notice%}}

## Instalación de chocolatey

1. Primero es asegurarnos que estamos corriendo una [consola administrativa](https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/) de PowerShell. La forma más fácil de ejecutarla es con el atajo `Ctrl+WinKey` (WinKey es la tecla de windows del teclado), un menú se abrirá del lado izquierdo donde podemos seleccionar la opción `Windows PowerShell (Admin)`.

2. Instala con powershell.exe

{{%notice warning%}}
**NOTA:** Asegurate de inspeccionar [https://chocolatey.org/install.ps1](https://chocolatey.org/install.ps1) antes de ejecutar cualquiera de los comandos abajo por seguridad. Chocolatey afirma que es seguro, pero tu deberías de verificar siempre la seguridad y contenido de **cualquier** script que provenga del internet y que no estés familiarizado. Todos estos comandos descargan un script para PowerShell y lo ejecutan en tu máquina. En Chocolatey se toman la seguridad muy en serio. [Lee mas sobre los protocolos de seguridad de Chocolatey](https://chocolatey.org/security).
{{%/notice%}}

Con PowerShell, debes asegurar que [Get-ExecutionPolicy](https://go.microsoft.com/fwlink/?LinkID=135170) no esta restringido. Te sugiero usar `Bypass` para sobrepasar la politica y poder instalar la cosas o `AllSiged` para un poco más de seguridad.

-   Ejecuta `Get-ExecutionPolicy`. Si regresa `Restricted`, entonces ejecuta `Set-ExecutionPolicy AllSigned` o `Set-ExecutionPolicy Bypass -Scope Process`.

Ahora ejecuta el siguiente comando:

```sh
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

3. Pega y ejecuta el comando de arriba y presiona _Enter_.

4. Espera algunos segundos a que el comando complete.

5. Si no sale ningún error, ya estas listo para utilizar Chocolatey. Escribe `choco` o `choco -?`, o ve a la [Guía de Uso](https://chocolatey.org/docs/getting-started) para más información.

## Instalar herramientas varias

### Instalando ACK

Para instalar el comando `ack`, en la misma PowerShell de arriba ejecuta `choco install -y ack`.

`ack` es una herramienta similar a [grep](https://www.tutorialspoint.com/unix_commands/grep.htm), optimizada para programadores. Diseñada para programadores con grandes arboles heterogéneos de código fuente, `ack` está escrito puramente en portable Perl 5 y toma la ventaja del poder de las expresiones regulares de Perl.

### Instalando TREE

Para instalar el comando `tree`, en la misma PowerShell de arriba ejecuta `choco install -y tree`.

`tree` es un programa de listado de directorios recursivo que produce un listado de archivos indentado por profundidad, este puede er colorizado si la variable de entorno `LS_COLORS` esta activa para la salida de la terminal (tty). Sin argumentos, `tree` lista los archivos en el directorio actual. Cuando se pasan argumentos de directorio, `tree` lista todos los archivos y/o directorios encontrados en el directorio indicado. Cuando se completa el listado de todos los archivos/directorios encontrados, `tree` regresa el numero total de archivos y/o directorios listados.
