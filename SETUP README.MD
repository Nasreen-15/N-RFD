<!DOCTYPE html>
<html>
<head>
    <title>RFD-TOOL Setup Guide</title>
</head>
<body>

<h2>Step 1: Create the App</h2>
<pre>
python manage.py startapp todo
</pre>

<h2>Step 2: Register the App</h2>
<p>Open: config/settings.py</p>
<pre>
INSTALLED_APPS = [
    ...
    "apps.todo",
]
</pre>

<h2>Step 3: Define the Model</h2>
<p>Open: todo/models.py</p>
<pre>
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
</pre>

<h2>Step 4: Run Migrations</h2>
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

<h2>Step 5: Create Views</h2>
<p>Open: todo/views.py</p>
<pre>
from django.shortcuts import render

def todo(request):
    return render(request, "todo.html")
</pre>

<h2>Step 6: Add URLs</h2>
<p>Create: todo/urls.py</p>
<pre>
from django.urls import path
from . import views

urlpatterns = [
    path("todo/", views.todo, name="todo"),
]
</pre>

<p>Open: config/urls.py</p>
<pre>

urlpatterns = [
    .......
    .......
    path("", include("apps.todo.urls")),
]
</pre>

<h2>Step 7: Create Template</h2>
<p>Create: todo/templates/todo/task_list.html</p>
<pre>
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
</pre>

<h2>Step 8: Add Menu Link</h2>
<p>Open: templates/includes/menu-list.html</p>
<pre>
<li><a href="{% url 'todo' %}" class="voss-btn">To‑Do List</a></li>
</pre>

</body>
</html>