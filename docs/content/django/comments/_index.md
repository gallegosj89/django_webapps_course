---
title: Comentarios
weight: 10
---

Actualmente, solamente tenemos un modelo de Post, ¿Qué si queremos recibir retro alimentación de nuestros lectores y dejarlos comentar?

### Modelo de comentarios

Vamos a abrir `blog/models.py` y pega esta pieza de código al final del archivo:

```python
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
```

Puedes ir atrás a la sección de [modelos]({{< ref "../models" >}}) si necesitas refrescar lo que cada tipo de campo significa. En esta práctica vamos a tener un nuevo tipo de campo:

-   `models.BooleanField` - Es un campo de tipo cierto/falso.

La opción `related_name` en `models.ForeignKey` nos permite enlazar y tener acceso a los comentarios desde el modelo Post.

### Migrando los cambios

Es tiempo de agregar nuestro modelo de comentarios a la base de datos. Para hacer esto le vamos a decir a Django que revise los cambios de nuestro modelo. Escribe `python manage.py makemigrations blog` en tu línea de comandos. Deberías ver algo como esto:

{{%notice warning%}}
Recuerda entrar al directorio de tu proyecto, puedes llegar allí con `cd ~/django-daw` o `cd %userprofile%\django-daw`. Despues inicia el entorno virtual.
{{%/notice%}}

```bash
(env) ~/django-daw$ python manage.py makemigrations blog
Migrations for 'blog':
  0002_comment.py:
    - Create model Comment
```

Como puedes ver, se ha creado otro archivo de migración en la carpeta `blog/migrations/`. Ahora necesitamos aplicar estos cambios escribiendo `python manage.py migrate blog` en la línea de comandos. La salida debería verse así:

```bash
(env) ~/django-daw$ python manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Rendering model states... DONE
  Applying blog.0002_comment... OK
```

Nuestro modelo de comentarios existe ahora en la base de datos, revisemos el modelo en el panel de administrador.

### Registra el nuevo modelo

Para registrar el modelo _Comment_ en el panel de administrador, ve a `blog/admin.py` y agrega esta línea:

```python
admin.site.register(Comment)
```

Justo debajo de esta línea:

```python
admin.site.register(Post)
```

Recuerda que es importante importar el modelo de comentarios al comienzo del archivo, se vera así:

```python
from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
```

Si escribes `python manage.py runserver` en la línea de comandos y vas a `http://127.0.0.1:8000/admin/` en tu navegador, ahora podrás acceder a la lista de comentarios, y también tendrás la posibilidad de agregar y eliminar comentarios.

![admin-comment.png](admin-comment.png?height=250px)

### Muestra los comentarios

Ve al template `post_detail.html` y agrega el siguiente código antes de la etiqueta `{% endblock %}`:

```html
<hr />
{% for comment in post.comments.all %}
<div class="comment">
    <div class="date">{{ comment.created_date }}</div>
    <strong>{{ comment.author }}</strong>
    <p>{{ comment.text|linebreaks }}</p>
</div>
{% empty %}
<p>Sin comentarios :(</p>
{% endfor %}
```

Ahora puedes ver la sección de comentarios en los detalles del post.

![no_comments.png](no_comments.png?height=400px)

Pero puede verse un poco mejor, así que vamos a agregar algún CSS al final de nuestra hoja de estilos `static/css/blog.css`:

```CSS
.comment {
    margin: 20px 0px 20px 20px;
}
```

También vamos a dejar a los visitantes ver un contador sobre los comentarios que dejan en la página. Ve al archivo `post_list.html` y agrega una línea como esta:

```html
<a href="{% url 'post_detail' pk=post.pk %}" class="pull-right">Comentarios: {{ post.comments.count }}</a>
```

Tu plantilla debería verse así:

```html
{% extends 'blog/base.html' %} {% block content %} {% for post in posts %}
<div class="post">
    <div class="date">{{ post.published_date }}</div>
    <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
    <p>{{ post.text|linebreaksbr|truncatechars:200 }}</p>
    <a href="{% url 'post_detail' pk=post.pk %}" class="pull-right">Comentarios: {{ post.comments.count }}</a>
</div>
{% endfor %} {% endblock content %}
```

![comment_count.png](comment_count.png?height=250px)

### Añade comentarios

Ahora podemos ver los comentarios hechos en nuestro blog, pero no podemos agregarlos. Cambiemos eso.

Ve a `forms.py` y agrega las siguientes líneas al final del archivo:

```python
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'author',
            'text',
        )
```

Recuerda importar el modelo Comentario, cambiando la línea:

```python
from .models import Post
```

aa:

```python
from .models import Post, Comment
```

Ahora vamos a la plantilla  `post_detail.html` y antes de la línea `{% for comment in post.comments.all %}`, agrega:

```html
<a class="btn btn-default" href="{% url 'add_comment_to_post' pk=post.pk %}">Agregar comentario</a>
```

Si quieres ir a los detalles del post, deberías ver este error:

![1801-url_error](1801-url_error.png?height=150px)

Ahora sabemos como arreglarlo. Ve a `blog/urls.py` y agrega este nuevo patron de URL:

```python
path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
```

Refresca la página y ahora tenemos un error diferente.

![1802-views_error](1802-views_error.png?height=150px)

Para agregar este error, agrega esto a `blog/views.py`:

```python
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
```

Recuerda importar `CommentForm` al comienzo del archivo:

```python
from .forms import PostForm, CommentForm
```

Ahora vamos a los detalles de la página y deberíamos ver el botón "Add Comment":

![add-comment.png](add-comment.png?height=100px)

Sin embargo, cuando des click en el botón verás:

![1804-template_error](1804-template_error.png?height=150px)

Como el error nos dice, la plantilla no existe aún. Entonces vamos a crear la plantilla `add_comment_to_post.html` y agregar el siguiente código:

```html
{% extends 'blog/base.html' %} {% block content %}
<h1>Nuevo comentario</h1>
<form method="POST" class="post-form">
    {% csrf_token %} {{ form.as_p }}
    <input type="submit" class="btn btn-default" value="Enviar" />
</form>
{% endblock %}
```

![comment_new.png](comment_new.png?height=400px)

Ahora nuestros lectores puede agregar lo que piensan en nuestros post.

### Modera los comentarios

No todos los comentarios deberían ser mostrados. Como dueño del blog, posiblemente quieras la opción de aprobar o eliminar comentarios. Vamos a hacer algo sobre esto.

Ve a la plantilla `post_detail.html` y cambia las líneas:

```html
{% for comment in post.comments.all %}
<div class="comment">
    <div class="date">{{ comment.created_date }}</div>
    <strong>{{ comment.author }}</strong>
    <p>{{ comment.text|linebreaks }}</p>
</div>
{% empty %}
<p>Sin comentarios :(</p>
{% endfor %}
```

a:

```html
{% for comment in post.comments.all %} {% if user.is_authenticated or comment.approved_comment %}
<div class="comment">
    <div class="date">
        {{ comment.created_date }} {% if user.is_authenticated %}
        <a class="btn btn-default" href="{% url 'comment_remove' pk=comment.pk %}"><span class="glyphicon glyphicon-remove"></span></a>
        {% endif %} {% if not comment.approved_comment %}
        <a class="btn btn-default" href="{% url 'comment_approve' pk=comment.pk %}"><span class="glyphicon glyphicon-ok"></span></a>
        {% endif %}
    </div>
    <strong>{{ comment.author }}</strong>
    <p>{{ comment.text|linebreaks }}</p>
</div>
{% endif %} {% empty %}
<p>Sin comentarios :(</p>
{% endfor %}
```

Deberías ver un `NoReverseMatch`, porque no hay ningún patrón de URL que concuerde con `comment_remove` y `comment_approve` aún. Para arreglar este error, agregamos estos patrones de URL a `blog/urls.py`:

```python
path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
```

Ahora deberías ver un `AttributeError`. Para arreglar este error, agrega las siguiente vistas en `views.py`:

```python
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
```

Necesitas importar Comment al comienzo del archivo:

```python
from .models import Post, Comment
```

Hay un pequeño cambio que podemos hacer. en nuestra página de lista -- debajo de posts -- actualmente vemos el número de los comentarios que el post ha recibido. Vamos a cambiar esto para que los usuarios no autenticados vean solo el número de comentarios aprobados.

Para arreglar esto, ve a `blog/templates/blog/post_list.html` y cambia la línea:

```html
<a href="{% url 'post_detail' pk=post.pk %}">Comentarios: {{ post.comments.count }}</a>
```

a:

```html
{% if user.is_authenticated %}
<a href="{% url 'post_detail' pk=post.pk%}">Comentarios: {{ post.comments.count }}</a>
{% else %}
<a href="{% url 'post_detail' pk=post.pk%}">Comentarios: {{ post.approved_comments.count }}</a>
{% endif %}
```

finalmente, añade el método `approved_comments` al modelo `Post` en `blog/models.py`:

```python
def approved_comments(self):
    return self.comments.filter(approved_comment=True)
```

Ahora puedes ver la característica de comentarios finalizada.

## Desplegar a producción

De nuevo; hemos hecho cambios en nuestro ambiente de desarrollo, hicimos algunas pruebas, y todo funciona correctamente. Es momento de desplegar la aplicación a nuestro servidor de producción.

Primero haz un punto de salvado (`commit`) de tu nuevo código, y haz `push` a tu repositorio remoto.

```bash
cd ~/django-daw
git status
git add .
git status
git commit -m "se agregó la funcionalidad de comentarios"
git pull
git push
```

Luego en una [consola Bash de PythonAnywhere](https://www.pythonanywhere.com/consoles/), descarga el nuevo código.

```bash
cd ~/gallegosj89.pythonanywhere.com
git pull
```

Inicia el entorno virtual en tu instancia de PythonAnywhere con `workon <project>` y recuerda que al ser bases de datos diferentes, la local y la remota, aquí también tienes que migrar los cambios como lo hiciste antes con `makemigrations` y `migrate`.

Debido a los cambios de hojas de estilos también hay que actualizar la colección de archivos estáticos.

```bash
python manage.py collectstatic
```

Finalmente, ve a la pestaña [Web](https://www.pythonanywhere.com/web_app_setup/) y haz click en **Reload**.
