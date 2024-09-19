# Learning Django @2024
A simple project to learn Django

> **Note :**
> - I will rely on [Create a Web Application With Django](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django) course from Openclassrooms
    for this mini-project and then summarize what I have learned.
>
> - I will use [ChatGPT](https://chat.openai.com/) to provide a summary with a simple storytelling technique, making
    this document accessible and easy to understand even for novices.

## Chapter 1 : Intro

Let me take you on a journey into the world of **Django**, a powerful open-source **Python framework** built for web development. 🌍🐍

**Django** is designed to help developers create web applications quickly, without sacrificing quality. ⚡ Throughout this course, you'll be guided step-by-step in creating a real, fully functional web app using Django. 🚀

We begin by building the foundation of your app with the **MVT** (Models, Views, and Templates) architecture. 🛠️ The **model** handles your data, **views** control what the user sees, and **templates** determine how it’s presented. 💾👁️🎨

Next, you’ll learn to manage data through Django's built-in admin interface. 🛡️ You'll then move on to developing your own interface to Create, Read, Update, and Delete (CRUD) data. 🔄

By the end of the course, you’ll be equipped with the skills to start building and managing Django apps, ready to launch your career as a Django web developer. 💻✨

### Learn From a Professional Scenario
In this course, you will create a full web application from start to finish. The context of this web application is outlined below:

You’ve been asked to create a proof of concept for a new web app: the Merch Exchange. This will be an app where people can list various collectible music merchandise like records, posters, and gig tickets. In addition, users should be able to post listings of the merch they would like to sell.

### Coming Back to the Project After a Restart

You should always have your `virtual environment activated` during development. For example, if you restart your machine and then come back to the project, you can activate your virtual environment by first making sure you’re in the directory that contains your  env  directory and the running: 

```bash
source env/bin/activate
```
### If Your Site Has Stopped Working

Sometimes while you're coding, you might notice that your Django development `server stops working`. But don’t worry—this happens often during development. 

**Here's why:**

The development server is set to automatically reload whenever it detects that you’ve saved changes to your files. This is helpful most of the time, but if your code is incomplete, the server might try to reload unfinished work and crash. 💥

Some IDEs, like PyCharm, even have an `auto-save` feature that can cause the server to reload without you manually saving your work. The good news is that the server process usually waits for your next code change and starts up again. 🔄

However, sometimes **the server can't recover from an error**. In that case, finish the code you're working on and follow these steps:

1. Get back to the terminal prompt by pressing `Ctrl + C` to stop the server. ⌨️
2. Make sure you’re in the right directory—use `ls` to check if you can see the `manage.py` file. If not, navigate to the correct folder using `cd`. 📂
3. Once you’re in the right directory, restart the server with `./manage.py runserver`. 🚀

If you don’t see `manage.py`, you're likely in the wrong directory. Use `ls` and `cd` to find it and restart your server.

---

## Chapter 2 : SetUp the environment

### 2.1 Install Django With pip

Before you can start building a Django web application, you need to install Django. Here's how you can do it, step by step:

1. **Open a terminal**: This is where you'll be running commands to set up Django. 💻

2. **Navigate to your projects directory**: Go to the folder where you typically store your projects. If you don’t have one, now’s a great time to create it! 🗂️

   Example:
   ```
   → cd projects/
   ```

3. **Create a directory for your Django project**: This will house all the files related to your web app. After creating the directory, navigate into it. 📁

   ```
   → mkdir django-web-app
   → cd django-web-app
   ```

4. **Initialize Git** (if you're using it): This step is optional, but highly recommended for tracking changes in your project. 🔄

   ```
   → git init
   ```

5. **Set up a virtual environment**: Virtual environments help keep your project’s dependencies isolated from other projects. 🌐

   ```
   → python -m venv env
   ```

6. **Activate the virtual environment**: This step ensures that any Python packages you install will be restricted to this project. 🛠️

   ```
   → source env/bin/activate
   ```

7. **Install Django using pip**: Now that your environment is ready, install Django using pip, the Python package manager. 📦

   ```
   (env) → pip install django
   ```

8. **Track your dependencies**: Create a `requirements.txt` file to list all the packages your project relies on. This makes it easier to recreate the environment in the future. 📑

   ```
   → pip freeze > requirements.txt
   ```

Now Django is installed, and you're all set to start building your web application! 🚀

---

## Chapter 3: Set Up a New Django Project

After setting up your environment and installing Django, it’s time to create the foundational structure for your web application.

### 3.1 Generate the Project Structure

Now that Django is installed, the next step is to generate the necessary files for your project. Instead of manually creating folders and files, Django provides a command-line tool to automate this process. 🎉

In the terminal, navigate to your project directory (where you created your `django-web-app` folder). Use the following command to create the base structure of your project:

```bash
django-admin startproject merchex
```

This command generates essential project files, including a new directory named `merchex` and a script called `manage.py`. The `merchex` directory will hold the main settings and configuration files for your app, while `manage.py` is the go-to tool for running Django commands. 

With just one command, you’ve laid the groundwork for your Django project! 🚀

### 3.2 Running the Development Server

With the basic structure in place, you can now launch the project on a development server. This allows you to see your application live, even if it's just the default Django page for now. 🌐

To start the server, use the following command:

```
python manage.py runserver
```

Once executed, Django will provide a local web address **([http://127.0.0.1:8000/](http://127.0.0.1:8000/))** where you can preview your app in a browser. 

At this stage, you should see the default Django page confirming that your project is running successfully. 🎨

![Running the Development Server](docs/images/part2-start-project.png)

### 3.3 Setting Up the Database

When you first start the server, Django may alert you about pending database migrations. These migrations are necessary to set up the application’s database, which will eventually store all your data.

To apply these migrations and create the database, run:

```
python manage.py migrate
```

This will create a database file named `db.sqlite3`, which holds all the data for your project. It’s a good practice to add this file to your `.gitignore` so it isn’t tracked in your version control system. 📂

### 3.4 Creating Your First App

In Django, a project is made up of several "apps," each focusing on a specific part of your application. For example, to handle **merchandise listings**, you’ll create an app called `listings`. This modular approach keeps your code organized as your project grows. 🛠️

To create the `listings` app, use:

```
python manage.py startapp listings
```

A new folder named `listings` will appear, containing the necessary files to start developing features related to merchandise listings.

### 3.5 Installing the App

After creating your app, you need to tell Django about it. Open the `settings.py` file inside the `merchex` directory and find the `INSTALLED_APPS` list. Add `'listings'` to this list to ensure Django includes it when running the project.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # New Apps
    'listings',
]
```

Your app is now officially part of the project, and you're ready to start building your first features! 🎉

---

## Chapter 4: Serve Content With a View

Now that your Django project is set up, it's time to bring it to life by displaying content on a webpage. 🚀 In this chapter, you’ll learn how to create web pages by using *views* and *URL patterns*, which are fundamental parts of Django’s architecture.

### 4.1 Create Your First View

In Django, a *view* is a Python function that takes a user’s request and sends back a response. This is how content is served to users. Let’s start by creating a simple view that displays a message.

1. **Open `views.py`**: Inside the `listings` app, locate `views.py`. Replace the default comment with a new function called `hello`, and import the `HttpResponse` class.

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')
```

🎉 You've just created your first view! This function will send back an HTML header saying "Hello Django!" whenever it's accessed.

### 4.2 Connect the View to a URL

Next, you need to connect this view to a specific URL. This is done by creating a *URL pattern*.

2. **Edit `urls.py`**: Open `merchex/urls.py` and add a new path that links the `/hello/` URL to the `hello` view. Don’t forget to import the view from the `listings` app.

```python
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
]
```

Now, when you visit ([http://127.0.0.1:8000/hello/](http://127.0.0.1:8000/hello/)) in your browser, your `hello` view will display its message. 🎉

### 4.3 The Role of URLs in Django

Every time a user interacts with your site, it begins with a URL. Django uses these URLs to match user requests with the correct view. You’ve already created one URL pattern, but let’s create another for an "About Us" page.

3. **Add a New View**: In `views.py`, add a second function called `about` to handle requests for the "About Us" page.

```python
def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love merch!</p>')
```

4. **Update URLs**: Add this new view to your URL patterns by editing `urls.py`.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('about-us/', views.about),
]
```

Once done, visit ([http://127.0.0.1:8000/about-us/](http://127.0.0.1:8000/about-us/)) to see the "About Us" page! 🖥️

### 4.4 Understanding Views and URL Patterns

Views and URL patterns work together to make your Django site interactive. The URL pattern tells Django which view to call based on the user’s request. While it may seem like magic when the view is automatically executed, this is actually Django handling everything behind the scenes. 🧑‍💻

### 4.5 Try It Yourself

Now that you’ve created two pages, it’s time to practice by adding more. Create two new pages: one for **merchandise listings** and one for **contact information**. Follow the same steps: define views in `views.py` and link them to URLs in `urls.py`. 

By the end of this chapter, you’ll have multiple pages running on your site, and you’ll be well on your way to mastering Django! 🎉

---