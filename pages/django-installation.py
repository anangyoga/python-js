import streamlit as st

st.set_page_config(page_title="Django Installation", page_icon="📝")

st.title("Django Installation")
st.page_link("main.py", label="Back to Homepage", icon="🏠")

st.divider()

st.write("Django is opinionated, so there are rules & conventions to follow. The architectural pattern is Model, View, Template. Model is for Database Operation, View is for Business Logic,and  Template is for Presentation Layer")

st.write("### Initiate Project")

st.write("To initiate the project, we can start by running these following commands:")

st.code(f""" 
1. python -m venv .venv
2. source ./.venv/Scripts/activate (Windows)
3. pip install django
""")

st.write("Django is now ready to go.")

st.write("### Create Root Project")

st.write("It's not convention, but mas Indra suggests to use :blue-background[core] or :blue-background[config] as the directory root of the project.")

st.code(f""" 
django-admin startproject core .
""")

st.write("Note: use :blue-background[. [dot]] after project's name so it didn't create directory-ception.")
st.write("Now you have :blue-background[core] directory.")
st.write("Let's initiate a project as the :blue-background[core] directory is the root of the app. We can start by running this command:")

st.code(f""" 
./manage.py startapp -nameapp
""")

st.write("This command will create another directory in-line with the :blue-background[core] directory.")

st.write("### Add the newly-created App on Settings")

st.write("Before writing any code. Go to the :blue-background[core] directory and find :blue-background[settings.py] file. Define your app on `INSTALLED_APPS` list.")

st.write("Something like this:")

st.code(f""" 
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    # your app
    'notes',
]
""")

st.write("### Views")

st.write("Views is the template where users can see the app on browser. On your :blue-background[views.py], you can define functions (or routes?) like this:")

st.code(f""" 
from django.shortcuts import render

# Create your views here.
def index_view(request):
  return render(request, "index.html")

def dashboard_view(request):
  return render(request, "dashboard.html")

def profile_view(request):
  return render(request, "profile.html")
""")

st.write("Now we need a place to collect all the html files. Hence, create a directory inside your app, it's a :blue-background[templates] directory. Inside it, you can create as many html files as you want.")

st.write("### Dispatcher")

st.write("Dispatcher is like a file where we can define all the routes after creating the html files. Under the same app, create :blue-background[urls.py] and write your dispatcher there.")

st.code(f""" 
from django.urls import path
# import your view here
from .views import index_view, profile_view

urlpatterns = [
  path("", index_view, name="index"),
  # always ends with slash /
  path("profile/", profile_view, name="profile")
  # always ends with slash /
  path("dashboard/", dashboard_view, name="dashboard")
]
""")

st.write("### Run Server")

st.write("I think everything is setup at this point. It's time to run the server to see the Views. Run it using this command:")

st.code(f""" 
./manage.py runserver
""")

st.write("We can follow the url in terminal and open it on browser.")

st.write("### Create Models")

st.write("We can define the ORM in the :blue-background[models.py] file. Create something like:")

st.code(f""" 
from django.db import models

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=250)
  # nullable 
  content = models.TextField(blank=True, null=True)
  # required
  seo_meta = models.TextField()
""")

st.write("At this point, we can just run :blue-background[./manage.py migrate] cause it's a fresh start.")
st.write("But when we add a new variable, like `created_at` below:")

st.code(f""" 
from django.db import models

# Create your models here.
class Note(models.Model):
  ......

  # new variable (or a column??)
  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
""")


st.write("We need to run :blue-background[./manage.py makemigrations] and then :blue-background[./manage.py migrate]. This way we don't mess up the data migration.")

st.write("Run the server again using: :blue-background[./manage.py runserver].")
st.write("On :blue-background[http://localhost:8000/admin/], you won't be able to see your app there.")

st.write("### Create a Superuser")

st.write("Inside you app directory (not the :blue-background[core] directory), find :blue-background[admin.py] file. You can register your app there.")

st.code(f""" 
from django.contrib import admin
# import your models
from .models import Note

# Register your models here.
admin.site.register(Note)
""")

st.write("Now turn off your terminal (or open a new one) and run the command below:")

st.code(f""" 
./manage.py createsuperuser
""")

st.write("On terminal, create username. You can skip email and it will fallback to username. Create the password as well. If the password is not unique, you can just ignore the warning and move on.")

st.write("Now you can run the server and check :blue-background[http://localhost:8000/admin/] to do CRUD on your app name.")

st.write("I found out that 🏃‍♂️:red[`php artisan` is to Laravel as `./manage.py` is to Django].")
st.write("That's all.")

if st.button("Back to Homepage"):
  st.switch_page("main.py")