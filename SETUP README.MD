## RFD-TOOL Setup Guide

### Step 1: Create the App

```
python manage.py startapp todo apps/todo

```
### Step 2: Register the App - Open: config/settings.py

```
INSTALLED_APPS = [
    ...
    "apps.todo",
]

```
### Step 3: Define the Model - Open: todo/models.py

```
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```
### Step 4: Run Migrations

```
python manage.py makemigrations
python manage.py migrate

```
### Step 5: Create Views - Open: todo/views.py

```
from django.shortcuts import render

def todo(request):
    return render(request, "todo.html")

```

### Step 6: Add URLs in todo/urls - Create: todo/urls.py if not

```
from django.urls import path
from . import views

urlpatterns = [
    path("todo/", views.todo, name="todo"),
]

```

### Step 7: Add Config URLs - Open: config/urls.py

```
urlpatterns = [
    .......
    .......
    path("", include("apps.todo.urls")),
]

```
### Step 8: Create Template - Create: todo/templates/todo/task_list.html (enter your UI code with must {% extends "layouts/base.html" %} header)

```
{% extends "layouts/base.html" %}
{% block content %}
<div class="container-fluid full-dashboard">
  <h2>My To-Do List</h2>
  <ul class="list-group">
    {% for task in tasks %}
      <li class="list-group-item {% if task.completed %}list-group-item-success{% endif %}">
        <strong>{{ task.title }}</strong> - {{ task.description }}
        {% if task.due_date %}
        <span class="badge badge-info">Due: {{ task.due_date }}</span>
        {% endif %}
      </li>
    {% empty %}
      <li class="list-group-item">No tasks yet.</li>
    {% endfor %}
  </ul>
</div>
{% endblock %}

```

### Step 9: Add Menu Link - Open: templates/includes/menu-list.html

```
<li><a href="{% url 'todo' %}" class="voss-btn">To‑Do List</a></li>

```