---
title: Extendiendo plantillas
weight: 7
---

Otra cosa buena que Django tiene para tí es la **extensión de plantillas**. Esto significa que puedes combinar varias plantillas para crear una página más compleja, además de poder reutilizar las plantillas para construir diferentes páginas de tu sitio web. De esta forma no tienes que repetir el código en cada uno de los archivos cuando quieres usar una misma información o un mismo esquema, por ejemplo importar bootstrap, tus hojas de estilos, o tu favicon. Y si quieres cambiar algo, no necesitas hacerlo en todas las plantillas.

### Crea la plantilla base

Una plantilla base es la plantilla que nos servira de boilerplate (código base o estructural) para todas las demás plantillas, esta la extiendes en cada otra pantilla de tu aplicación.

Vamos a crear un archivo `base.html` en `blog/templates/blog/`:

```txt
blog
└───templates
    └───blog
            base.html
            post_list.html
```

Luego ábrelo y copia todo lo que hay en `post_list.html` al archivo `base.html`, de la siguiente manera:

```html
{% load static %}
<html>
    <head>
        <title>DAW blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Crimson+Text:wght@600&display=swap" />
        <link rel="stylesheet" href="{% static 'css/blog.css' %}" />
        <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}" />
    </head>
    <body>
        <div class="page-header">
            <h1><a href="/">DAW Blog</a></h1>
        </div>

        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                    {% for post in posts %}
                    <div class="post">
                        <div class="date">{{ post.published_date }}</div>
                        <h2><a href="">{{ post.title }}</a></h2>
                        <p>{{ post.text|linebreaksbr }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </body>
</html>
```

Luego, en el archivo `base.html` reemplaza por completo lo que hay dentro de la etiqueta `<body>` (todo lo que haya entre `<body>` and `</body>`) con esto:

```html
<body>
    <div class="page-header">
        <h1><a href="/">DAW Blog</a></h1>
    </div>
    <div class="content container">
        <div class="row">
            <div class="col-md-8">{% block content %} {% endblock %}</div>
        </div>
    </div>
</body>
```

Básicamente remplazamos todo entre `{% for post in posts %} {% endfor %}` con:

```python
{% block content %} {% endblock %}
```

Acabas de crear un `block` (con el template tag `{% block %}`), este es básicamente un marcador que indica que cualquier plantilla hija, es decir otras plantillas que extiendan a `base.html`, van a poner su contenido en ese espació. Verás como hacer esto en un momento.

{{%notice info%}}
Para saber más sobre las _template tags_ (etiquetas de plantilla) de Django visita la [documentación oficial](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/).
{{%/notice%}}

Ahora vas a cambiar al archivo `post_list.html` de nuevo. Elimina todo arriba de `{% for post in posts %}` y debajo de `{% endfor %}`, y agrega la línea `{% extends 'blog/base.html' %}` al inicio del archivo. De forma que tu archivo se verá así:

```python
{% extends 'blog/base.html' %}

{% for post in posts %}
<div class="post">
    <div class="date">{{ post.published_date }}</div>
    <h2><a href="">{{ post.title }}</a></h2>
    <p>{{ post.text|linebreaksbr }}</p>
</div>
{% endfor %}
```

Esta primera línea indica a esta plantilla que va a extender a otra plantilla llamada `base.html`. Pero aun no le decimos a la plantilla `post_list.html` que sección es la a poner en el `block` que se definió en `base.html`, para esto tenemos que indicarlo envolviendo el contenido entre las etiquetas `{% block content %}` y `{% endblock %}`. De esta manera:

```python
{% extends 'blog/base.html' %}

{% block content %}

{% for post in posts %}
<div class="post">
    <div class="date">{{ post.published_date }}</div>
    <h2><a href="">{{ post.title }}</a></h2>
    <p>{{ post.text|linebreaksbr }}</p>
</div>
{% endfor %}

{% endblock %}
```

Eso es todo. Ahora verifica que tu sitio web aún funcione apropiadamente.

{{%notice warning%}}
Si tienes un error de tipo `TemplateDoesNotExists` que diga que no existe el archivo `blog/base.html` y ya tienes `runserver` ejecutándose en la consola, intenta detener (presionando `Ctrl + C`) y reiniciar el servidor (ejecuta `python manage.py runserver`).
{{%/notice%}}

{{%notice info%}}
Si quieres saber mas sobre como funciona la extensión de plantillas puedes consultar la [documentación oficial](https://docs.djangoproject.com/en/3.1/ref/templates/language/#template-inheritance).
{{%/notice%}}

Si todo funciona hasta este punto igual que como funcionaba antes, no olvides crear un punto de guardado con Git.

```bash
cd ~/django-daw
git status
git add .
git status
git commit -m "se creo una plantilla base y se extendió en la plantilla post_detail"
git pull
git push
```

## Amplía tu aplicación

Ya hemos completado lsa bases para la creación de nuestro sitio web. Sabemos cómo escribir un modelo, agregar patrones de URL, crear vistas, y trabajar con plantillas. Entonces para no perder estos conocimientos vamos a ejercitarlos, lo primero que necesitamos en nuestro blog es, obviamente, una página donde mostrar un solo post, para en caso de que sea muy largo y no queramos mostrar todo su contenido en la página principal.

Ya tenemos un modelo `Post`, así que no necesitamos añadir nada a `models.py`.

### Añade una URL al título

Vamos a empezar añadiendo una URL dentro del archivo `blog/templates/blog/post_list.html`. Queremos tener un enlace en el titulo del post que nos lleve a una página donde se vea con detalle el contenido. Vamos a cambiar la linea `<h2><a href="">{{ post.title }}</a></h2>`, añadiéndole contenido al atributo `href` (_hypertext reference_ o referencia de hipertexto):

```html
<h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
```

Te explicar que significa este misterioso tag `{% url 'post_detail' pk=post.pk %}`:

-   Como probablemente sospeches, la notación `{% %}` significa que estamos utilizando Django template tags. Esta vez vamos a utilizar uno que va a crear una dirección URL para nosotros.
-   La parte `post_detail` es donde le decimos a Django el nombre del patron URL que va a usar para poner aquí, buscará en `blog/urls.py` el patron que tenga el parametro `name=post_detail`.
-   Para entender que es `pk=post.pk` debemos saber que `pk` es abreviatura de _primary key_ (llave primaria), este es el nombre de una propiedad de todos los objetos que heredan de la clase `Model` (como lo es nuestra clase `Post`). Ya que no especificamos una llave primaria en nuestro modelo `Post`, Django crea una para nosotros. Por defecto, es un numero que incrementa en uno para cada entrada en la base de datos, y lo añade como un campo llamado `pk` a cada uno de nuestros posts. Nosotros podemos acceder a la llave primaria escribiendo `post.pk`, de la misma manera que accedemos a otros campos (`title`, `author`, etc.) de nuestro objeto `Post`.

{{%notice info%}}
Si quieres saber mas sobre la propiedad `pk` puedes consultar la [documentación oficial](https://docs.djangoproject.com/en/3.1/ref/models/instances/#the-pk-property).
{{%/notice%}}

Ahora cuando vayamos a: <http://127.0.0.1:8000/> tendremos un error, esto es de esperarse, puesto que no hemos creado el patron URL de nombre `post_detail` ni la vista que le corresponde. El error deberia verse así:

![no_reverse_match.png](no_reverse_match.png?height=250px)

### Crea el patron URL `post_detail`

Vamos a crear un patron de URL en `blog/urls.py` para que apunte a nuestra vista `post_detail`. Supongamos que queremos que el detalle de nuestro primer post sea mostrado en esta URL: <http://127.0.0.1:8000/post/1/>.

Queremos crear un patron de URL que le diga a Django que queremos llamar una vista de nombre `post_detail`, que va a mostrar una entrada del blog. Para esto agrega la línea `path('post/<int:pk>/', views.post_detail, name='post_detail'),` al archivo `blog/urls.py`. Debería quedar ocmo abajo y a hroita te explico que significa `'post/<int:pk>/'`.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
```

Esta parte `post/<int:pk>/` especifica un patron de URL — te lo explico:

-   `post/` significa que la URL debe de empezar con la palabra **post** seguido de una **/**. Hasta aquí todo bien.
-   `<int:pk>` — esta parte es un poco mas complicada. Significa que Django espera un valor de tipo entero y que lo transferirá a una vista como una variable llamada `pk`.
-   `/` — necesitamos agregar **/** de nuevo para terminar la URL.

Eso significa que si entras en `http://127.0.0.1:8000/post/5/` en tu navegador, Django procesara el string `post/5/`, el cual coincidirá justo con este patron que estamos definiendo, ya que despues de la primer `/` hay un numero entero `5`, y termina con una `/`. Entonces Django mandará llamar a la vista de nombre `post_detail` y transferirá la el `5` ala vista en un parametro con el nombre `pk`.

Bien, hemos añadido un nuevo patron de URL a `blog/urls.py`. Actualiza la página: <http://127.0.0.1:8000/> ¡Boom! El servidor a dejado de funcionar. Mira la consola — como era de esperarse, hay otro error.

![attribute-error.png](attribute-error.png?height=150px)

¿Te acuerdas del próximo paso? Crear la función `post_detail` que leerá nuestro post de la base de datos y llamará una pantilla para mostrarlo en el navegador.

### Crea la vista `post_detail`

Esta vez nuestra vista (a diferencia de `post_list`) recibirá un parámetro adicional de nombre `pk`. Así que definiremos nuestra función como `def post_detail (request, pk):`. Ten en cuenta que tenemos que usar exactamente el mismo nombre que especificamos en el patron URL (`pk`). Omitir esta variable es incorrecto y resultará en un error. Como solo queremos sólo un post del blog y no toda una lista como la vista `post_list`, necesitamos un queryset que tome el objeto de la base datos en base a su llave primaria - será algo como `Post.objects.get(pk=pk)`.

Si eres un tanto perspicaz, te estarás preguntando ¿Y que pasa si en `pk` va un identificador de un objeto que no existe? (ej. `38956`), en este caso tu aplicación funcionará - pero mostrará una pagina de error como la siguiente.

![does-not-exist.png](does-not-exist.png?height=150px)

Entonces necesitamos una forma de validar que el `pk` recibido es valido antes de hacer nuestro queryset, para esto Django incluye una libreria con que se encargará del problema por nosotros llamada `get_object_or_404`. Con esta, en caso de que no haya ningún `Post` con el `pk` indicado, se mostrará una página mucho más conocida del código http `404`.

![page-not-found.png](page-not-found.png?height=150px)

La buena noticia es que puedes crear tu propia página para el código `404` y diseñarla como desees. Pero por ahora no es tan importante, así que lo dejaremos para otra sección.

Ya que tenemos toda esta información vamos a añadir el código que necesitamos para nuestra vista al archivo `views.py`. Primero importaremos la libreria antes mencionada.

```python
from django.shortcuts import render, get_object_or_404
```

Y despues al final del archivo añadimos el código de nuestra vista. Guardamos y actualizamos.

```python
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

![no-errors.png](no-errors.png?height=450px)

Sin errores. Pero, ¿qué pasa cuando haces clic en el enlace de un título?

![template-does-not-exists.png](template-does-not-exists.png?height=150px)

Otro error. Pero es uno que ya habíamos visto antes, y sabemos que solo tenemos que crear la plantilla indicada.

Crearemos un archivo en `blog/templates/blog` llamado `post_detail.html`. Se verá así:

```html
{% extends 'blog/base.html' %} {% block content %}
<div class="post">
    {% if post.published_date %}
    <div class="date">{{ post.published_date }}</div>
    {% endif %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.text|linebreaksbr }}</p>
</div>
{% endblock %}
```

Una vez más estamos extendiendo `base.html`. En el bloque `content` queremos mostrar la fecha de publicación (si existe), título y texto de nuestros posts. Comó es esta diferente de `post_list.html`, pues a qui no tenemos un bucle `for` porque solo solo recibimos un objeto `post` y no una lista de objetos `posts`. Ademas de que aquí introducimos otro template tag importante `{% if ... %} ... {% endif %}`, este lo podemos usar igualq ue como funcionan `if/else` en Python, y nos sirve para evaluar condiciones. En este escenario queremos comprobar si el campo `published_date` de un post existe, es decir si no es un valor `Null`.

Listo, por fin podemos actualizar nuestra página y ver el resultado de nuestro trabajo.

![post_detail.png](post_detail.png?height=250px)

## Sube tus cambios a producción

Ya que haz hecho cambios locales, y las pruebas necesarias para confirmar que tu aplicación funciona, es hora de desplegar la aplicación a nuestro servidor de producción, es decir _PythonAnywhere_.

```bash
cd ~/django-daw
git status
git add .
git status
git commit -m "se añadieron los patrones, vistas y templates para mostrar el detalle de un post"
git pull
git push
```

Luego, ve a _PA_ y en una [consola Bash](https://www.pythonanywhere.com/consoles/) ejecuta los siguientes comandos.

```bash
cd ~/gallegosj89.pythonanywhere.com
git pull [...]
```

{{%notice warning%}}
Recuerda sustituir `~/gallegosj89.pythonanywhere.com` con el nombre correcto de tu directorio en PythonAnywhere.
{{%/notice%}}

### Actualizando los archivos estáticos del servidor

Servidores como PythonAnywhere prefieren tratar los archivos estáticos (como los archivos CSS) de manera diferente a los archivos de Python, ya que pueden crear optimizaciones para cargarlos mas rápido. Como resultado, cada vez que hacemos cambios a nuestros archivos CSS, tenemos que ejecutar comandos extra en el servidor para actualizarlos, el comando es llamado `collectstatic`.

Comienza activando tu entorno virtual (si no esta activo todavía), recuerda que PythonAnywhere utiliza un comando llamado `workon` para hacer esto, es lo mismo que el comando `source env/Scripts/activate` que usas en Git Bash, así:

```bash
workon gallegosj89.pythonanywhere.com
cd ~/gallegosj89.pythonanywhere.com
python manage.py collectstatic
```

El comando `manage.py collectstatic` es similar a `manage.py migrate`. Nosotros realizamos cambios en el código, y después le decimos a Django que aplique esos cambios, ya sea a la colección de archivos estáticos del servidor, o a la base de datos.

Ya esta todo listo para ir a la pestaña [Web](https://www.pythonanywhere.com/web_app_setup/) y hacer click en **Reload**.
