---
title: Seguridad
weight: 9
---

Nuestro blog ha recorrido un largo camino para llegar a este punto, pero aún hay espacio para la mejora. Lo siguiente que haremos será agregar nuevas características para poder crear borradores de posts y publicarlos de manera posterior, ademas de añadir una forma de eliminar posts.

### Crear posts sin publicarlos

Actualmente, cuando creamos nuevos post usando nuestro formulario, el post es publicado directamente al guardar. Vamos a modificar esta lógica un poco para guardar el post como borrador, **elimina** estas líneas de código en `blog/views.py` que se encuentran en las vistas `post_new` y `post_edit`:

```python
post.published_date = timezone.now()
```

Con esto los nuevos post no serán publicados automáticamente con la fecha y hora actual, esto deja nuestra aplicación con la funcionalidad un poco limitada, pero lo resolveremos en un momento.

### Página de borradores

En la sección de [querysets]({{< ref "../views/#querysets" >}}) vimos como solicitar objetos de la base de datos, posteriormente en la sección de [vistas]({{< ref "../views/#datos-dinámicos-en-las-plantillas" >}}) creamos la vista `post_list` que muestra solamente los post publicados (aquellos que tienen un `publication_date` no vacío).

Es tiempo de hacer algo similiar, pero con borradores. Vamos a añadir un botón con enlace en `blog/templates/blog/base.html` en el encabezado. No queremos mostrar nuestros borradores a todo el mundo, entonces vamos a colocarlo dentro de la validación de usuarios autenticados (`{% if user.is_authenticated %}`), justo después del botón de agregar posts.

```html
<a href="{% url 'post_draft_list' %}" class="top-menu"><span class="glyphicon glyphicon-edit"></span></a>
```

Ahora crearemos el nuevo patron de URL `post_draft_list` en `blog/urls.py`:

```python
path('drafts/', views.post_draft_list, name='post_draft_list'),
```

Después crearemos la nueva vista en `blog/views.py`:

```python
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
```

Esta línea de código `posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')` se asegura de que solamente vamos a tomar objetos de tipo `Post` que no cuentan con fecha de publicación (`published_date__isnull=True`) y los ordena por fecha de creación (`order_by('created_date')`). Y por último creamos la plantilla. Crea un archivo `blog/templates/blog/post_draft_list.html` y agrega lo siguiente:

```html
{% extends 'blog/base.html' %} {% block content %} {% for post in posts %}
<div class="post">
    <p class="date">creado: {{ post.created_date|date:'d-m-Y' }}</p>
    <h2><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h2>
    <p>{{ post.text|truncatechars:200 }}</p>
</div>
{% endfor %} {% endblock %}
```

Esta plantilla se ve muy similar a nuestro `post_list.html`. Ahora cuando vayas a `http://127.0.0.1:8000/drafts/` vas a ver la lista de post no publicados.

![post_draft_list.png](post_draft_list.png?height=350px)

{{%notice tip%}}
**Tip**
\
Si deseas que en tu página principal no salga tanto texto en tus posts (plantilla `post_list.html`), y que solo puedan ser visualizados por completo en la plantilla `post_detail.html`, agrega a la linea donde se muestra el texto del post (`<p>{{ post.text|linebreaksbr }}</p>`) la opción de truncado y el número de caracteres a los cuales quieres truncar (por ejemplo 200 caracteres `truncatechars:200`) y debería verse de esta manera `<p>{{ post.text|linebreaksbr|truncatechars:200 }}</p>`.
{{%/notice%}}

### Botón para publicar

Sería bueno tener un botón en el detalle del post que publique el post inmediatamente, para esto vamos a abrir `post_detail.html` y cambiar estas líneas:

```html
{% if post.published_date %}
<div class="date">{{ post.published_date }}</div>
{% endif %}
```

por estas:

```html
{% if post.published_date %}
<div class="date">{{ post.published_date }}</div>
{% else %}
<a class="pull-right btn btn-default" href="{% url 'post_publish' pk=post.pk %}"
    ><span class="glyphicon glyphicon-check"></span
></a>
{% endif %}
```

Como puedes ver, hemos agregado la línea `{% else %}`. Esto significa, que la condición de `{% if post.published_date %}` no es cumplida (no hay fecha de publicación), entonces se aplicará la línea `<a class="pull-right btn btn-default" href="{% url 'post_publish' pk=post.pk %}"><span class="glyphiconglyphicon-check"></span></a>`. Nota que estamos pasando la variable `pk` en la etiqueta `{% url %}`. Es tiempo de crear un nuevo patrón de URL (en `blog/urls.py`):

```python
path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
```

Y finalmente una vista (como siempre, en `blog/views.py`):

```python
def post_publish(request, pk):
  post = get_object_or_404(Post, pk=pk)
  post.publish()
  return redirect('post_detail', pk=pk)
```

Recuerda, cuando creamos la clase del modelo `Post` escribimos un método `publish`, se veía como esto:

```python
def publish(self):
  self.published_date = timezone.now()
  self.save()
```

Ahora finalmente podemos utilizarlo al dar clic en el botón para _aprovar_, entonces seremos redirigidos inmediatamente a la página `post_detail.html` del post indicado.

![post_publish.png](post_publish.png?height=300px)

### Botón para eliminar

Vamos a abrir `post_detail.html` de nuevo y vamos a añadir esta línea justo sobre la línea del botón editar:

```html
<a class="pull-right btn btn-default" href="{% url 'post_remove' pk=post.pk %}"
    ><span class="glyphicon glyphicon-remove"></span
></a>
```

Ahora necesitamos un patrón de URL (`blog/urls.py`):

```python
path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
```

Ahora, abre `blog/views.py` y agrega este código:

```python
def post_remove(request, pk):
  post = get_object_or_404(Post, pk=pk)
  post.delete()
  return redirect('post_list')
```

La única cosa nueva en realidad es el método para eliminar el post (`post.delete()`). Cada modelo en Django puede ser eliminado con el método `delete()`. Después de eliminar un post, queremos ir a la página principal con la lista de posts, por eso usamos el método `redirect`. Probemos, ve a la página de detalle de alguno de tus posts e intentemos eliminar uno.

![post_delete.png](post_delete.png?height=300px)

## Asegurando el sitio web

Puedes haberte dado cuenta que no usaste tu contraseña, además de cuando iniciaste en la interfaz de administrador. También debes haber notado que esto significa que cualquiera puede editar tus post en tu blog. No se tu, pero a mi no me gustaría que cualquiera editara mi blog, así que vamos a hacer algo al respecto.

### Autorización

Primero vamos a hacer las cosas un nivel más seguras. Vamos a proteger nuestras vistas `post_new`, `post_edit`, `post_draft_list`, `post_remove` y `post_publish` para que solo usuarios que hayan iniciado sesión puedan acceder a ellas. Python y Django nos proveen algunas herramientas para hacer esto posible, los llamados _decoradores_ (_decorators_). El decorador que vamos a usar está en el módulo `django.contrib.auth.decorators` y es llamado `@login_required`, el cual solo permite utilizar una vista si el usuario ha hecho login.

{{%notice info%}}
Para saber más sobre los decoradores de Django visita [la página oficial](https://docs.djangoproject.com/en/3.1/topics/http/decorators/).
{{%/notice%}}

Entonces editemos `blog/views.py` y agrega estas líneas al comienzo del archivo (donde importamos los módulos necesarios):

```python
from django.contrib.auth.decorators import login_required
```

Entonces añade la siguiente línea antes de cada una de las vistas `post_new`, `post_edit`, `post_draft_list`, `post_publish`, y `post_remove`, (decorándolas) como a continuación:

```python
@login_required
def post_new(request):
  [...]
```

Eso es todo. Ahora intenta acceder a <http://localhost:8000/post/new/>. ¿Notas la diferencia?

![login_required.png](login_required.png?height=300px)

{{%notice warning%}}
Si obtienes un formulario vacío, posiblemente haz hecho login en la interfaz de administrador. Ve a <http://localhost:8000/admin/logout/> para salir, y luego regresa a <http://localhost:8000/post/new> de nuevo.
{{%/notice%}}

Esto es muy interesante: el decorador que añadimos nos _redireccionará_ a la página de login, pero como no hemos creado ninguna, retorna un error `404` _Page not found_.

No te olvides del decorador encima de `post_edit`, `post_remove`, `post_draft_list` y `post_publish` también.

Ahora otras personas no podrán acceder a las página seguras de nuestro blog. Desafortunadamente, nosotros tampoco podemos crearlos (a menos que iniciemos sesión en el administrados de Django).

### Autenticación

Ahora podemos intentar hacer muchas cosas mágicas para implementar usuarios, contraseñas, y autenticación. Como Django viene con _"baterías incluidas"_, alguien ya ha hecho el trabajo duro por nosotros, así que vamos a utilizar las herramientas que nos provee Django.

En los patrones de URL del sitio `mysite/urls.py` (**no** `blog/urls.py`) agrega un nuevo patrón de URL `path('accounts/login/', auth_views.LoginView.as_view(), name='login')`. Así el archivo debería verse similar a este:

```python
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('', include('blog.urls')),
]
```

Luego necesitamos agregar una plantilla para la página de ingreso, así que crearemos el directorio `blog/templates/registration` y dentro un archivo llamado `login.html`.

```html
{% extends "blog/base.html" %} {% block content %} {% if form.errors %}
<p>Tu usuario y contraseña no pudieron ser corroborados. Por favor intenta de nuevo.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <table>
        <tr>
            <td>{{ form.username.label_tag }}</td>
            <td>{{ form.username }}</td>
        </tr>
        <tr>
            <td>{{ form.password.label_tag }}</td>
            <td>{{ form.password }}</td>
        </tr>
    </table>

    <input type="submit" value="Entrar" />
    <input type="hidden" name="next" value="{{ next }}" />
</form>
{% endblock %}
```

Verás que también hace uso de la plantilla base para mantener el estilo de tu blog. Como puedes ver no necesitamos lidiar con el manejo de formularios, las contraseñas y asegurarlas.

![login.png](login.png?height=200px)

Solamente una cosa mas para hacer, vamos a la configuración en `mysite/settings.py` y definimos una nueva constante `LOGIN_REDIRECT_URL`:

```python
LOGIN_REDIRECT_URL = '/'
```

Esto hace que despues de hacer login, se redirecciona al usuario a la página de primer nivel, en nuestro caso `post_list.html`.

## Añadiendo el botón de login

Ya definimos como autorizar usuarios. Vemos los botones para añadir post. Ahora queremos asegurarnos que el botón de ingreso les aparezca a todos los usuarios Podemos agregar el botón de ingreso con esta línea:

```html
<a href="{% url 'login' %}" class="top-menu"><span class="glyphicon glyphicon-lock"></span></a>
```

Para esto necesitamos editar la plantilla base, así que vamos a abrir `base.html` y modificarla de tal manera que la parte dentro de `<body>` se verá así:

```html
<body>
    <div class="page-header">
        {% if user.is_authenticated %}
        <p class="top-menu">
            <a href="{% url 'logout' %}" class="top-menu"><span class="glyphicon glyphicon-log-out"> </span></a>
            <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
        </p>
        {% else %}
        <a href="{% url 'login' %}"><span class="glyphicon glyphicon-log-in"></span></a>
        {% endif %}
        <h1><a href="/">DAW Blog</a></h1>
    </div>

    <div class="content container">
        <div class="row">
            <div class="col-md-8">{% block content %} {% endblock %}</div>
        </div>
    </div>
</body>
```

Debes reconocer el patrón aquí. Hay una condición _if_ en la plantilla que verifica si el usuario está autenticado para mostrar los botones de agregar y editar, de otra manera, se muestra el botón de login.

![login_button.png](login_button.png?height=150px)

## Mostrar el usuario autenticado

Vamos a agregarle un poco de azúcar a nuestras plantillas mientras estamos en esto. Primero vamos a mostrar algunos detalles de cuando ingresamos. Editemos el archivo `base.html` así:

```html
<body>
    <div class="page-header">
        {% if user.is_authenticated %}
        <p class="top-menu">
            <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
            <a href="{% url 'post_draft_list' %}" class="top-menu"><span class="glyphicon glyphicon-edit"></span></a>
            Hola {{ user.username }}
            <a href="{% url 'logout' %}" class="top-menu"><span class="glyphicon glyphicon-log-out"> </span></a>
        </p>
        {% else %}
        <a href="{% url 'login' %}"><span class="glyphicon glyphicon-log-in"></span></a>
        {% endif %}
        <h1><a href="/">DAW Blog</a></h1>
    </div>

    <div class="content container">
        <div class="row">
            <div class="col-md-8">{% block content %} {% endblock %}</div>
        </div>
    </div>
</body>
```

Esto agrega un mensaje "**Hola _user.username_**" para recordarle al usuario con que cuenta ingresó, y que en este momento está autenticado. También agrega un enlace de salida del blog -- como puedes ver, aún no funciona.

Decidimos apoyarnos en Django para manejar el ingreso, así que vamos a dejar que Django se encargue de la salida. Vamos a agregar un patrón de URL en `mysite/urls.py` apuntando a la vista de salida (`django.contrib.auth.views.LogoutView`) así:

```python
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
  path('', include('blog.urls')),
]
```

No olvides agregar la configuración de redirección después del logout en `mysite/settings.py`:

```python
LOGOUT_REDIRECT_URL = '/'
```

{{%notice info%}}
Para más información sobre el sistema de autenticación de django revisa la [documentación oficial](https://docs.djangoproject.com/en/3.1/topics/auth/default/).
{{%/notice%}}

Y finalmente para que no se vean unos botones muy grandes y amontonados, podemos modificar la clase `.top-menu` es nuestra hoja de estilos (`blog.css`) así:

```css
.top-menu,
.top-menu:hover,
.top-menu:visited {
    color: #ffffff;
    float: right;
    font-size: 16pt;
    margin-right: 5px;
    margin-left: 5px;
}
```

![logout_button.png](logout_button.png?height=150px)

Si has seguido todo lo anterior, en este punto, tu blog ahora:

-   Permite al usuario hacer login utilizando su nombre de usuario y contraseña
-   Tiene un nivel de seguridad donde solo permite a usuarios que han hecho login: agregar, editar, publicar o eliminar posts
-   Permite al usuario hacer logout
