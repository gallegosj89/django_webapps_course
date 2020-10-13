---
title: Máquina virtual (deprecated)
description: Deprecated
weight: 99
subpage: false
hidden: true
---

# Instalación de máquina virtual

Requisitos:

-   Disco o imagen de instalación de Debian:

    -   [debian-9.1.0-i386-netinst.iso](https://cdimage.debian.org/debian-cd/current/i386/iso-cd/debian-9.3.0-i386-netinst.iso "Imagen ideal cuando se tiene conexión de red")

-   Archivo de instalación de [VirtualBox](http://download.virtualbox.org/virtualbox/5.1.26/VirtualBox-5.1.26-117224-Win.exe "v5.1.26")

    > Nota: Usar la imagen `netinst` de preferencia, se necesita una conexión estable a Internet.

## Preparación

Una vez adquiridas la/las imágenes de Debian y tener VirtualBox instalado. Se procede a crear la máquina virtual. Para esto se siguen los pasos a continuación:

1.  En la barra de tareas de VirtualBox se le da click en el icono de `New`.

    ![barra de herramientas de VB](0107-vb_menu.png)

2.  Se abrirá una nueva ventana que indica `Create Virtual Machine`, los parámetros a introducir se muestran en la imagen a continuación:

    ![VB create window](0108-vb_create.png)

    > Note. En caso de que la ventana no sea iguala la imagen anterior es probable que el menú avanzado no este activado, para activarlo oprima el botón **Expert Mode**.

    Al terminar de configurar oprimir el botón **Create**.

3.  La siguiente ventana tendrá como titulo `Create Virtual Hard Disk`, se configurará de la siguiente manera:

    ![VB create HDD](0109-vb_hdd.png) Al terminar oprima el botón **Create**.

4.  Ahora de nuevo en la ventana principal, oprima el icono `Settings` (engrane) de la barra de herramientas. En la nueva ventana ir a la pestaña `Advanced`; en esta ventana fijar los elementos `Shared Clipboard` y `Drag'n'Drop` a _`Bidirectional`_. Esto se muestra en la siguiente imagen:

    ![VB bidirectional setting](0110-vb_bidirec.png)

5.  En esta misma ventana de `Settings` ir al menú de `Storage` del lado izquierdo. Seleccionar el elemento nombrado como `Empty` debajo de `Controller: IDE`. Al lado derecho de la ventana aparecerá un icono de disco, hacer click en el y después en `Choose Virtual Optical Disk File...`. En la nueva ventana buscan la imagen `iso` del disco de instalación de Debian:

    ![VB iso selection](0111-vb_iso.png)

    Al hacerlo la ventana se verá de la siguiente manera:

    ![VB disk window](0112-vb_disk.png)

    Dar click en el botón **OK**.

6.  El siguiente pasó consiste en arrancar la máquina virtual, para esto se da click en el botón **Start** de la barra de herramientas de VirtualBox.

7.  Una vez iniciada la máquina virtual, para hacer la vista más cómoda ir al menú `View -> Scalated Mode` y después maximizar la ventana.

    ![VB scalate](0113-vm_scalate.png)

8.  Ahora con la máquina virtual corriendo elegir la opción `Graphical Install` y la instalación de GNU/Linux distribución Debian comenzará.

## Procedimiento

1.  La primera pantalla de instalación será `Select a language`, oprimir el botón **Continue**.

2.  La pantalla muestra _Select your location_, oprimir el botón **Continue**.

3.  La pantalla muestra `Configure the keyboard`, si el teclado contiene la letra `ñ` seleccionar `Latin American`, de otra manera deje la opción por defecto `American English`. oprimir el botón **Continue**.

4.  Iniciará una etapa de configuración para continuar con la instalación.

5.  La pantalla muestra `Configure the network` y dentro tiene el campo _`Hostname`_. Escribir el hostname `debian` y oprimir el botón **Continue**.

6.  La pantalla sigue mostrando `Configure the network` solo que ahora tiene el campo _`Domain name`_. Dejar en blanco y oprimir el botón **Continue**.

7.  La pantalla muestra `Set up users and passwords` y contiene dos campos _`Root password`_ y _`Re-enter password to verify`_. Escribir dentro de los campos la misma contraseña `password`. oprimir el botón **Continue**.

8.  La pantalla sigue mostrando `Set up users and passwords` solo que ahora contiene un solo campo _`Full name for the new user`_, aquí puedes poner tu nombre o en el caso de esta guía escribir `daw`. Oprimir el botón **Continue**.

9.  La pantalla sigue mostrando `Set up users and passwords` solo que ahora contiene el campo _`Username for your account`_, escribir `daw` y oprimir el botón **Continue**.

10. La pantalla sigue mostrando `Set up users and passwords` solo que ahora contiene los campos _`Choose a password for the new user`_ y _`Re-enter password to verify`_, escribir `password` en los dos campos. Oprimir el botón **Continue**.

11. La pantalla muestra `Configure the clock`, en esta pantalla se selecciona `Pacific` y se oprime el botón **Continue**.

12. La pantalla muestra `Partition disks`, seleccionar `Guided - use entire disk` y oprimir el botón **Continue**.

13. La pantalla sigue mostrando `Partition disks`, solo debe haber una opción así que oprimir el botón **Continue**.

14. La pantalla sigue mostrando `Partition disks`, seleccionar la opción `All files in one partition (recommended for new users)` y oprimir el botón **Continue**.

15. La pantalla sigue mostrando `Partition disks`, seleccionar la opción `Finish partitioning and write changes to disk` y oprimir el botón **Continue**.

16. La pantalla sigue mostrando `Partition disks`, aparece una pregunta _`Write the changes to disks?`_ seleccionar `Yes` y oprimir el botón **Continue**.

17. Se iniciara la instalación del sistema base.

18. Al terminar, la pantalla mostrará `Configure the package manager` y preguntará _`Scan another CD or DVD?`_ seleccionar la opción `No` y oprimir el botón **Continue**.

19. La pantalla sigue mostrando `Configure the package manager`, seleccionar la opción `United States` ya que es el servidor más cercano a nosotros y oprimir el botón **Continue**.

20. La pantalla sigue mostrando `Configure the package manager`, seleccionar la opción `ftp.us.debian.org` y oprimir el botón **Continue**.

21. La pantalla sigue mostrando `Configure the package manager`, en la pantalla se encuentra un solo campo _`HTTP proxy information (blank or none)`_; dejar en blanco y oprimir el botón **Continue**.

22. El proceso continuara aplicando las configuraciones.

23. La pantalla mostrará `Configuring popularity-contest` y contendrá la pregunta `Participate in the package usage survey?`, seleccionar la opción `Yes` y oprimir el botón **Continue**.

24. La pantalla ahora muestra `Software selection`, esta pantalla es muy importante aquí se deben seleccionar las siguientes opciones:

-   Debian desktop environment
-   ... GNOME
-   print server
-   SSH server
-   standard system utilities Estas opciones instalaran algunos elementos necesarios para trabajar, además de la interfaz grafica de GNOME. Oprimir el botón **Continue**.

    > Nota. En sistemas con recursos limitados seria buena opción instalar `Xfce` en lugar de `GNOME`

25. La instalación continuara. Este paso puede tardar largo tiempo dependiendo de la conexión a internet y los recursos de la máquina. Así que aprovecha para ir por un café o un snack.

26. Una vez terminada la instalación de los paquetes esenciales la pantalla muestra `Install the GRUB boot loader on a hard disk`. En pantalla se muestra la pregunta `Install the GRUB boot loader to the master boot record?`, selecciona la opción `Yes` y oprime el botón **Continue**.

27. La pantalla sigue mostrando `Install the GRUB boot loader on a hard disk`, selecciona la segunda opción `/dev/sda`. Oprime el botón **Continue**.

28. La instalación finalizara después de esto. Oprimir el botón **Continue** y la máquina virtual se reiniciará.

## Post-instalación

En este punto la máquina debe de estar instalada de manera satisfactoria y al reiniciar se deberá hacer login utilizando el usuario y contraseña `daw:password`, o en su defecto los utilizados durante la instalación.

Lo primero será crear un acceso directo a la terminal, para esto ir a la esquina superior izquierda `Activities -> Show applications -> Settings`.

![Gnome settings location](0115-vm_settings.png)

Ahora en la ventana de `Settings` ir a `Keyboard`, hacer scroll hasta el final y oprimir el botón **+**. Ahora en la ventana de `Add custom shortcut` introducir los siguientes datos:

-   Name: Terminal
-   Command: gnome-terminal
-   Shortcut: Oprimir el botón **Set Shortcut** y ejecutar el comando `Ctrl+Alt+T`.

Cerrar todo y ejecutar el comando para comprobar que efectivamente abre la terminal. Una vez abierta se puede cambiar el color de esta desde `Edit -> Preferences -> Theme variant`.

Por ultimo comprobar que el comando `sudo ls` se ejecuta correctamente. De lo contrario diríjase a la sección de _Troubleshooting_.

## Troubleshooting

### Error `sudo: command not found` o similar

Para resolver este error tenemos que entrar a modo administrador, para esto en una terminal ejecuta `su` e introduce la contraseña `password`. Ahora instalaremos `sudo` con el comando `apt-get install sudo`. Para que el comando lo podamos usar después desde nuestro usuario normal, tenemos que darle acceso al grupo `sudo` - ejecutemos el comando `adduser daw sudo` y para terminar reiniciamos la máquina virtual con `reboot`.
