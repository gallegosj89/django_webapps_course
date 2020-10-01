---
title: Configuración
weight: 1
---

{{% alert theme="warning" %}}HUGO **v0.50** minimum required to use this theme (prefer extended version if you want to modify this theme source{{%/alert%}}

{{% alert theme="info" %}}Last version of HUGO is recomended, tests are always done with the last version.{{%/alert%}}

The following steps are here to help you initialize your new website. If you don’t know Hugo at all, we strongly suggest you to train by following this [great documentation for beginners](https://gohugo.io/overview/quickstart/).

<!--more-->

We assume that all changes to Hugo content and customizations are going to be tracked by git (GitHub, Bitbucket etc.). Develop locally, build on remote system.

## Requisitos

La siguiente es una lista de los requisitos necesarios para trabajar en un correcto ambiente de trabajo pra Python y Django. Descarga la version correspondiente con tu sistema operativo (32 o 64 bits).

En caso de que utilices algun Software de restauración de sistema (e.j. Deep Freeze), instala estas herraminetas antes de habilitarlo. Toma en cuenta que al utilizar un software como este deberas respaldar el folder de trabajo en prácticas posteriores.

-   [cmder](https://cmder.net/): Descarga la version mini, ya que instalaremos Git mas adelante
-   [python](https://www.python.org/downloads/): Descargar una version igual o mayor a 3.7.4
-   [gnuwin32](http://getgnuwin32.sourceforge.net/): Descargar la version mas reciente
-   [vscode](https://code.visualstudio.com/): Descargar la version mas reciente
-   [git](https://git-scm.com/downloads): Descargar la version mas reciente
-   [pip](https://pip.pypa.io/en/stable/): El enlace es para el manual de referenca, la instalacion se hara por medio de Python modules mas adelante
-   [viertualenv](https://virtualenv.pypa.io/en/latest/): El enlace es para el manual de referenca, para la instalacion se utilizarán Python modules mas adelante

## Proceso de instalación

Las siguientes subsecciones decriben como instalar y configurar cada uno de los requisitos arriba mencionados.

### Console Emulator

Agregar en Settings>Launcher? `/dir \"C:/Users/<Nombre de usuario>"` e.j. `/dir \"C:/Users/Carlos"`

Add bin folder to PATH in environment variables

### Python

Add bin folder to PATH in environment variables

#### Pip

`$ python -m pip install --upgrade pip --user`

#### Virtualenv

`$ python -m pip install virtualenv --user`

### GNUWin32

Para instalar GnuWin32:

1. Descarga el instalador desde [aqui](https://sourceforge.net/projects/getgnuwin32)

2. Descompriman el ejecutable en el lugar de su agrado ej. ~/Desktop

3. Entren al folder GetGnuWin32 doble clic en download.bat, sigan las instrucciones dela ventana. Este proceso tardará un buen tiempo, tomense un té.

4. Ahora de nuevo en el folder GetGnuWin32 doble clic en install.bat, sigan las instrucciones (yes to all).

5. De nuevo en el folder GetGnuWin32 debe de haber un nuevo folder con nombre gnuwin32, copiar este folder a C:/

6. Agregar C:/gnuwin32/bin a la variable Path.

Add bin folder to PATH in environment variables

### Visual Studio Code

Install python extention

### Git

## Configuración

Para crear nuestro folder de trabajo utilizaremos la terminal (cmder)

    mkdir django-daw
    cd django-daw
    python -m virtualenv myvenv

Para probar que está funcionando ejecutaremos los siguientes comandos: (Recuerden estos comandos de ahora en adelante)

    ./myvenv/Scripts/activate
    deactivate
