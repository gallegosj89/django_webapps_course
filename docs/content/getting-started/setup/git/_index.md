---
title: Git
weight: 4
---

Descarga el instalador de la versión más actual desde la [página de descargas](https://git-scm.com/downloads), asegurate de seleccionar el instalador indicado para tu sistema operativo, por ejemplo [Windows](https://git-scm.com/download/win).

{{%notice info%}}
Si estás en un sistema operativo diferente de Windows, sigue las instrucciones dependiendo si estas en [Linux/Unix](https://git-scm.com/download/linux) o [Mac OS X](https://git-scm.com/download/mac) de la página oficial.
{{%/notice%}}

Para la instalación en Windows, ejecuta el instalador y selecciona las opciones como en la siguiente imagen.

![0107-git_options](0107-git_options.png)

En la siguiente ventana selecciona `Use Visual Studio Code as Git's default editor`, para poder utilizar _Visual Studio Code_ como el editor por defecto de mensages de commit.

![0108-git_editor.png](0108-git_editor.png)

En la siguiente ventana selecciona `Git from the command line and also from 3rd-party software`, para poder utilizar el comando `git` tanto en la terminal por defecto `git-bash` como en otras terminales del sistema operativo (`cmd`, `powershell`, `terminal`).

![0109-git_console.png](0109-git_console.png)

En la siguiente ventana selecciona `Use the OpenSSL library`, para utilizar la libreria interna `OpenSSL` para la seguridad en la comunicación con servidores remotos.

![0110-git_ssl.png](0110-git_ssl.png)

En la siguiente ventana selecciona `Checkout Windows-style, commit Unix-style line endings` para que _Git_ se encargue de cambiar los finales de linea de los archivos de texto entre modo Windows y modo Unix, esto permite la compatibilidad del repositorio con otra plataformas (Linux, OSX).

![0111-git_line-endings.png](0111-git_line-endings.png)

En la siguiente ventana selecciona `Use MinTTY (the default terminal of MSYS2)` para que cuando sea requerido _Git_ utilice la terminal integrada `Git Bash` por defecto.

![0112-git_bash.png](0112-git_bash.png)

En la siguiente ventana selecciona `Default (fast-forward or merge)` para que _Git_ utilice esa técnica a la hora de hacer `pull` de un repositorio remoto.

![0113-git_pull.png](0113-git_pull.png)

En la siguiente ventana selecciona `Git Credential Manager Core` para que _Git_ utilice su sistema interno de manejo de credenciales.

![0114-git_credentials.png](0114-git_credentials.png)

En al siguiente ventana habilita las dos opciones disponibles; una para que se haga un cache interno de la aplicación y otra para que se habilite la creación de enlaces simbólicos (virtuales).

![0115-git_extra.png](0115-git_extra.png)

En la siguiente ventana habilita `Enable experimental support for pseudo consoles` para poder usar interpretes de comandos dentro de _Git Bash_.

![0116-git_experimental.png](0116-git_experimental.png)

Estas son toda las opciones de importancia, continua y termina la instalación.
