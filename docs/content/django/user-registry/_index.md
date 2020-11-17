---
title: Registro de usuarios
weight: 11
---

Hasta este momento la única forma de agregar usuarios es utilizando la linea de comandos o entrando al administrador de Django. Esta no es la manera ideal si queremos que un usuario pueda crear su propia cuenta desde el front end de nuestro sitio.

## Instalando _Crispy Forms_

Vamos a usar una librería llamada _Cryspi Forms_ que nos ayudara a dar una mejor presentación a nuestro formulario. Para instalarla utilizamos el instalador de paquetes de Python (pipx).

{{%notice warning%}}
Recuerda entrar al directorio de tu proyecto, puedes llegar allí con `cd ~/django-daw` o `cd %userprofile%\django-daw`. Despues inicia el entorno virtual.
{{%/notice%}}

```bash
pip install django-crispy-forms
```

Ahora modificamos nuestro archivo `settings.py` donde habilitaremos la librería. Primero busca la lista `INSTALLED_APPS` y modificarla para que se vea de la siguiente manera.

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "blog.apps.BlogConfig",
]
```

Ahora al final de tu archivo `settings.py` añade la siguiente linea:

```python
CRISPY_TEMPLATE_PACK="bootstrap3"
```

Le estamos diciendo a la librería de _Crispy Forms_ que utilizaremos Bootstrap version 3.

## Formulario de registro

Django incluye un formulario por defecto que podemos utilizar para registrar usuarios. En ocasiones futuras podríamos querer manipular los campos del formulario, para eso vamos a crear una instancia del formulario proveído por Django y agregarle campos que nos parezcan necesarios. Ve a `forms.py` en nuestro folder de `blog`, y agrega las siguientes lineas al inicio:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
```

Más abajo crea la clase de registro que va heredar del formulario que Django provee, y agregarle el campo `email`, de esta manera también tenemos el correo de los usuarios.

```python
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )
```

Como puedes ver hemos definidido que el formulario utilizará los campos del modelo `User`, que va a heredar del formulario `UserCreationForm` y hemos sido capaces de añadir un campo extra llamado "_email_", este nos puede servir en un futuro si queremos validar que un usuario que ya ha creado una cuenta utilizando un correo electrónico no pueda crear otra cuenta utilizando ese mismo correo. Esto ya queda de tu parte el implementarlo.

## La vista de registro

Ya que tenemos el formulario definido vamos a crear una plantilla donde podremos desplegar nuestro formulario. Crea el archivo `register.html` en el folder `blog/templates/registration`. Y añade el siguiente texto:

```html
{% extends "blog/base.html" %}

{% block title %}Crea tu cuenta{% endblock %}

{% load crispy_forms_tags %}

{% block content %}
<form method="POST" class="form-group">
    {% csrf_token %}
    {{ form|crispy }}
    <input type="submit" value="Registrar" />
</form>
{% endblock %}
```

Ahora necesitamos una vista que mande renderizar y maneje los datos proveídos por el formulario. Ve a `views.py` y agrega la siguiente vista al final del archivo:

```python
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
```

No olvides importar tu formulario a este archivo, modifica la linea al inicio del archivo para que se vea así:

```python
from .forms import PostForm, CommentForm, RegisterForm
```

Ahora para poder acceder a esta vista necesitamos registrar un patrón de URL, ve a `urls.py` que pertenece a `blog.py` y agrega el patrón `path("accounts/register", views.register, name="register"),` para que tus patrones se vean así:

```python
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit", views.post_edit, name="post_edit"),
    path("drafts/", views.post_draft_list, name="post_draft_list"),
    path("post/<int:pk>/publish", views.post_publish, name="post_publish"),
    path("post/<int:pk>/remove", views.post_remove, name="post_remove"),
    path("post/<int:pk>/comment", views.add_comment_to_post, name="add_comment_to_post"),
    path("comment/<int:pk>/approve", views.comment_approve, name="comment_approve"),
    path("comment/<int:pk>/remove", views.comment_remove, name="comment_remove"),
    path("accounts/register", views.register, name="register"),
]
```

Con esto podemos ejecutar nuestro servidor (`python manage.py runserver`) e ir al URL `http://localhost:8000/accounts/register` y registrar un nuevo usuario. No olvides seguir las reglas de Django para la creación de contraseñas, si fallas aparecerá un mensaje con el cual podrás saber por que falló la creación del usuario.

Ahora podemos agregar un botón a nuestra plantilla `login.html` para poder acceder a la pagina de registro. Añade esta linea justo sobre el botón de *Entrar*, en caso de que el usuario quiera registrarse primero.

```html
...
<p>¿No tienes una cuenta? ¡Crea una! <a href="{% url 'register' %}">aquí</a></p>
<input type="submit" value="Entrar" />
<input type="hidden" name="next" value="{{ next }}" />
...
```

## Desplegar a producción

De nuevo; hemos hecho cambios en nuestro ambiente de desarrollo, hicimos algunas pruebas, y todo funciona correctamente. Es momento de desplegar la aplicación a nuestro servidor de producción.

Primero haz un punto de salvado (`commit`) de tu nuevo código, y haz `push` a tu repositorio remoto.

```bash
cd ~/django-daw
git status
git add .
git status
git commit -m "se agregaron la funcionalidad de registro de usuarios"
git pull
git push
```

Luego en una [consola Bash de PythonAnywhere](https://www.pythonanywhere.com/consoles/), descarga el nuevo código.

```bash
cd ~/gallegosj89.pythonanywhere.com
git pull
workon gallegosj89.pythonanywhere.com
```

Aquí también tenemos que instalar el paquete _django-crispy-forms_.

```bash
pip install django-crispy-forms
```

Debido a los cambios de hojas de estilos también hay que actualizar la colección de archivos estáticos.

```bash
python manage.py collectstatic
```

Finalmente, ve a la pestaña [Web](https://www.pythonanywhere.com/web_app_setup/) y haz click en **Reload**.