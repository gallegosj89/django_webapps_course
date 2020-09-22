---
title: Troubleshooting
weight: 12
---

## Como recuperar su proyecto usando Github

Si se corrompió la maquina virtual, o su carpeta del proyecto, o simplemente formatearon su computadora y no respaldaron sus archivos de la maquina virtual. Este proceso les puede ayudar a recuperar su proyecto o la mayor parte de el, siempre y cuando hayan seguido las instrucciones y tengan todo respaldado en su repositorio remoto de Github. Si solo se corrompió la carpeta del proyecto, pueden borrarla y seguir los pasos del 3 en adelante.

1. Instalar/Importar la maquina virtual. Primero deben de tener una maquina virtual ya instalada y disponible en virtual box.

2. Asegurarse que estén todas las utilidades y software necesario para ejecutar proyectos en python/django/virtualenv. Ejecuten el siguiente comando:

```bash
sudo apt install git python3 python3-pip python3-virtualenv
```

3. Clonar el repositorio remoto. Ir a su cuenta de Github y copiar la dirección de su repositorio. Ahora utilizar el siguiente comando en su maquina virtual. Modificando el URL por el correcto de su repositorio, el `django-daw` al final del comando indica que este es el nombre que se le dará a la carpeta del proyecto.

![RP-github](/images/RP-github.PNG)

```bash
git clone https://github.com/gallegosj89/my-first-blog.git django-daw
```

4. Crear un ambiente virtual. Recuerda crear un ambiente virtual utilizando Python 3, dentro de la carpeta de su proyecto.

```bash
python3 -m venv django-daw/myvenv
```

5. Entrar a la carpeta de su proyecto, iniciar su ambiente virtual, e instalar el framework de Django.

```bash
cd django-daw
source myvenv/bin/activate
pip install django
```

6. Ejecutar los comando de inicialización de un proyecto de Django (p.e. migrar la base de datos).

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Ya con esto debería de funcionar su proyecto de manera normal. Como se mencionó antes, solo que hayas tenido respaldado en tu repositorio remoto. Otra cosa es que la base de datos no se respalda en el repositorio, por lo que tendrás que crear nuevos posts.

[1]: images/RP-github.png
