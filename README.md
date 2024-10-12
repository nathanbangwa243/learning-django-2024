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

## Chapter 5: Save Data to a Database With a Model and a Migration

Now that your Django project is up and running, it’s time to add some life by saving real data in the database. In this chapter, we will explore how Django uses **models** to represent entities and how **migrations** help us manage the database schema.

### 5.1 Creating a Model

In any web application, storing data is essential. Imagine you're building an app that tracks **bands** and their merchandise. Each of these is an entity, and in Django, you represent these entities with a **model**.

A model is like a blueprint, defining the information you want to store about an entity. For instance, the **Band** model might have fields like the band's **name**, **genre**, and the year they became active. These fields store the details you need.

**Here’s the cool part:** Django makes it super easy to create models using Python classes! 🎉 You define a class for each entity, and Django takes care of everything else, like saving data to the database. 

### 5.2 Adding Your First Model

To create the **Band** model, you simply edit the `models.py` file in your app. You define a class that inherits from Django's `models.Model`, which brings all the tools needed to interact with the database.

For example:
```python
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
```
In this case, we’ve created a field `name` to store the band’s name. Django will take care of adding this field to the database for us. 🎸

### 5.3 Applying Migrations to the Database

Now that you've defined the **Band** model, it’s time to make sure the database knows about it. This is where **migrations** come in. Migrations are Django’s way of translating your model changes into database schema updates. 🛠️

First, you need to generate a migration file that tells Django what changes to make:
```bash
python manage.py makemigrations
```
Django creates a migration file for the **Band** model. To apply this migration and update the database schema, run:
```bash
python manage.py migrate
```
Now, the database is ready to store bands! 🎉

### 5.4 Saving Data in the Django Shell

With the **Band** model and database schema set up, you can now add data. One way to do this is through the **Django shell**, which allows you to interact with your app's models in real-time.

Open the shell:
```bash
python manage.py shell
```
Create a new band:
```python
from listings.models import Band
band = Band(name='De La Soul')
band.save()
```
The `save()` method stores this new band in the database. Just like that, you’ve saved your first object to the database! 🎉

### 5.5 Displaying Data in the View

Now that the **Band** objects are stored in the database, how do we display them on a webpage? Simple. In your view, use `Band.objects.all()` to retrieve all bands and pass them to the template.

Here’s an example in your `views.py`:
```python
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>My favorite bands are:</p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
    """)
```
This code grabs the list of bands from the database and displays their names in an HTML list. 🎶

### 5.6 Now It’s Your Turn!

Try adding a new **listing** model for merchandise items. Give it a `title` field and practice using migrations to add it to the database. Then, use the Django shell to add a few **listing** objects and display them in your app.

---

## Chapter 6: Clean Separation of Logic and Presentation With Django Templates

After saving data to the database in the previous chapter, it’s time to improve how we display that data. Right now, our views are cluttered with HTML mixed into Python code. This can quickly become messy and hard to maintain, especially as your application grows. 

In this chapter, we’ll solve this problem by separating the logic from the presentation using **Django templates**.

### 6.1 The Problem with HTML in Views

When you mix your app’s logic (like retrieving data from the database) with HTML presentation in your views, the code becomes difficult to manage. 

For example, if you want to update the design of a webpage, you’ll need to dig through the Python code, which can be confusing and error-prone. 

**Here’s the solution:** Django provides a powerful way to separate concerns by using templates for the presentation layer. Templates handle all the HTML, while views focus on logic like fetching data. 🧹✨

### 6.2 Creating and Using a Template

To start cleaning up your views, you need to create a template file for the HTML. This file will be separate from the Python code, ensuring a clear distinction between what is displayed and how it’s processed. 📝💻

1. **Create the Template File**  
   First, create a new HTML file for your view in a `templates` folder (e.g., `listings/templates/listings/hello.html`). Inside this file, you can write your HTML as usual, without worrying about Python code. 🗂️📄

2. **Refactor the View**  
   Next, update the view in `views.py` to use the template. Instead of writing HTML in the view itself, you’ll use Django’s `render()` function to return a rendered template. This keeps the view focused on fetching data. Here’s an updated view:
   ```python
   from django.shortcuts import render
   from listings.models import Band

   def hello(request):
       bands = Band.objects.all()
       return render(request, 'listings/hello.html', {'bands': bands})
   ```
   🎨🔄

### 6.3 Using Template Variables

Once you’ve refactored the view, you’ll need to display the data in your template. Django makes this easy with **template variables**. For example, to show the name of each band, use double curly braces (`{{ }}`) in the HTML:
```html
<ul>
    {% for band in bands %}
        <li>{{ band.name }}</li>
    {% endfor %}
</ul>
```
Now, Django will replace `{{ band.name }}` with the actual band names from the database. 🎶🎤

### 6.4 Filters and Logic in Templates

Django templates also allow you to apply filters and use basic logic. For example, you can use the `upper` filter to display band names in uppercase:
```html
<li>{{ band.name|upper }}</li>
```
You can also add conditional logic, like an `if` statement, to customize the output based on the data:
```html
{% if bands|length > 0 %}
    <p>Here are my favorite bands:</p>
{% else %}
    <p>No bands to display.</p>
{% endif %}
```
💡🔄

### 6.5 A Clean and Maintainable Approach

By using templates, you keep your views simple and focused on data processing. The templates take care of rendering the HTML, making your app much easier to maintain and scale as you add more features. 🚀💻

🎉 You’re now equipped to build web pages that display dynamic content while keeping your code clean and organized!

---

## Chapter 7: Add Structure and Style to Your Site With a Base Template, CSS, and Static Files

Building on the foundation of clean logic and presentation from the previous chapter, it’s now time to refine your Django project further. As your app grows, managing multiple templates can become cumbersome, especially with repeated HTML code. 

In this chapter, we'll introduce **base templates**, **static files**, and **CSS**, helping you create a well-structured and visually appealing site. 🎨

### 7.1 The Challenge of Repeated Code

As you develop your app, you’ll notice many templates containing the same HTML structure, like `<html>`, `<head>`, and `<body>`. This repetition not only clutters your code but also makes it harder to manage changes. 

Imagine needing to update the title across several pages! This is where the **DRY principle**—Don’t Repeat Yourself—comes in handy. By utilizing a base template, you can centralize common HTML elements, making your code cleaner and easier to maintain. 🧹

### 7.2 Creating a Base Template

To start, you’ll create a **base template** that contains the shared HTML structure. This base template will serve as a foundation for all your other templates. 

**Here’s how:**

1. **Define Common HTML**  
   Create a new file called `base.html` in your `templates` folder. Include the common elements, such as the `<html>`, `<head>`, and a `{% block content %}` section for unique content:

   ```html
   <!-- listings/templates/listings/base.html -->
   <html>
       <head>
           <title>Merchex</title>
       </head>
       <body>
           {% block content %}{% endblock %}
       </body>
   </html>
   ```

2. **Inherit from the Base Template**  
   In your specific templates (like `hello.html`), you’ll now use the `{% extends 'listings/base.html' %}` tag at the top. This tells Django to build upon the base template, allowing you to focus only on the unique content for that page:

   ```html
   <!-- listings/templates/listings/hello.html -->
   {% extends 'listings/base.html' %}

   {% block content %}
   <h1>Hello Django!</h1>
   <p>My favorite bands are:</p>
   <ul>
       {% for band in bands %}
           <li>{{ band.name }}</li>
       {% endfor %}
   </ul>
   {% endblock %}
   ```

### 7.3 Adding Style with CSS

Now that your structure is solid, it’s time to enhance your site’s appearance with **CSS**. You’ll create a static file for your styles, which will ensure a consistent look across your application. Here’s how:

1. **Create a Static Folder**  
   Inside your app directory, create a folder named `static`, and within it, another folder for your CSS files (e.g., `listings/static/listings/`). 

2. **Link Your CSS File**  
   In your base template, add a `<link>` tag to connect your CSS file. Use Django’s `{% static %}` tag to ensure the file is correctly located when the site runs:

   ```html
   <link rel="stylesheet" href="{% static 'listings/styles.css' %}" />
   ```
   For the  `static`  tag to work, we first need to `load` it into this template. We do that by adding a  `load`  tag at the very beginning of the file, like this: 
   
   ```html
   {% load static %}
   <html>
   ...
   ```

3. **Create a CSS File**  
   In your `listings/static/listings/` folder, create a file called `styles.css`:

   ```css
   /* listings/static/listings/styles.css */
   body {
       background-color: red; /* Just for testing */
   }
   ```

### 7.4 Ensure Everything Works

Once your CSS file is linked, do a quick test to see if it loads correctly. Start your development server and check if your styles apply. If everything is set up right, you’ll have a stylish site that stands out! 🎉

### 7.5 Update All Templates

With a working base template and CSS, your next task is to ensure all your page templates inherit from the base template. Each template should include the `{% extends %}` and `{% block content %}` tags, keeping your code consistent and easy to manage. 🔧

### 7.6 Recap of MVT Architecture

This chapter reinforces the **MVT architecture**—Models, Views, and Templates—which keeps your application organized. By separating your application into these components, you facilitate teamwork and maintainability. Each developer can focus on their part without worrying about conflicting changes. 

### 7.7 Embracing Server-Side Rendering

Finally, it’s essential to understand the benefits of **server-side rendering**. This approach generates HTML on the server and sends it to the client, making it simpler to build and maintain your app. While client-side rendering is becoming popular, server-side rendering remains a great starting point, especially for proof-of-concept projects.

---

## Chapter 8: Capturing Data with Models and Fields 📋

In this chapter, we dive into **models** and **fields** in Django, focusing on how they help us structure data. Think of a **model** as a blueprint for an entity in your app. 

For example, we used a model for a music band. Each band has different characteristics like a name, genre, and year they were formed. These characteristics are stored in **fields**.

#### Model Example:
```python
from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year_formed = models.IntegerField()
    is_active = models.BooleanField(default=True)
```

Django provides different field types depending on the kind of data we want to store. Here's how we broke it down:

- **CharField**: For strings like the name and biography.
- **IntegerField**: Perfect for numbers, like the year the band was formed.
- **BooleanField**: A true/false field, used to mark if the band is still active.
- **URLField**: Specifically for web addresses.

Each field can have **options** or **rules**. For example, the name field has a maximum length, and the year must be between 1900 and 2021. If the band doesn't have a homepage, we allow that field to be left blank.

#### Field with Rules Example:
```python
class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year_formed = fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    website = models.URLField(blank=True)
```

### Adding Choices 🎛️

For certain fields, like genre, we may want to limit user input to a list of predefined choices (to avoid inconsistencies). Django's `TextChoices` class makes this possible. 

We defined genres such as Hip-Hop, Synth Pop, and Alternative Rock using this feature.

#### Choices Example:
```python
class GenreChoices(models.TextChoices):
    HIPHOP = 'HH'
    SYNTHPOP = 'SP'
    ALTERNATIVEROCK = 'AR'

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=2, choices=GenreChoices.choices)
```

### Migrating the Changes 🚀

Once new fields are added to a model, we must update the database to reflect these changes. This is done through a **migration**. 

Think of it as a way to keep the database in sync with the model. The `makemigrations` command checks for changes, and Django will sometimes ask for default values when non-optional fields are added.

#### Migration Commands:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Handling Defaults and Validations 🛠️

When we add new columns to an existing table, Django needs a way to fill in those values for existing records. For example:
- If the **biography** field is added, Django asks for a default value (we used an empty string).
- For **genre**, we chose Hip-Hop as a placeholder.
- The **year_formed** got a default value of 2000.

This way, we ensure every record is complete, even if the new fields were added later.

After that, we can apply the migration with the `migrate` command, and the database will now support the new structure! 🎉

### Conclusion

In this chapter, we learned how to capture data in Django using models and fields, and how to handle migrations and defaults. In the next part, we'll learn how to enforce users to input values in forms and handle data validation more robustly. 🧐

---

## Chapter 9: Perform CRUD Operations in the Django Admin 📊

Following our exploration of **models** and **fields** in the previous chapter, we now turn our attention to the next crucial aspect of data management: **CRUD operations**. 

These four operations—Create, Read, Update, and Delete—are essential for interacting with the data we've structured using Django's models.

### What is CRUD?

CRUD refers to the fundamental actions we can perform on data:

- **Create**: Inserting new records into the database.
- **Read**: Retrieving existing records for display or analysis.
- **Update**: Modifying existing records to reflect changes.
- **Delete**: Removing records that are no longer needed.

Up until this point, we have focused on creating and reading objects in the Django shell. Now, we will learn how to perform all four CRUD operations using Django’s built-in Admin interface, which simplifies these tasks significantly.

### Discovering the Django Admin Site

Django's Admin site is a powerful feature that allows developers and administrators to manage their models easily. To get started, we first create a superuser account with the following command:

```bash
python manage.py createsuperuser
```

This superuser will have the highest level of permissions, allowing us to access all features of the Admin site. After creating the superuser, we register our models—like the `Band` model—in the `admin.py` file. 

This registration makes the model manageable from the Admin interface:

```python
from django.contrib import admin
from listings.models import Band

admin.site.register(Band)
```

Once we run our development server and navigate to the Admin site at `http://127.0.0.1:8000/admin/`, we can log in and start managing our models.

### Performing CRUD Operations

1. **Create**: By clicking the “+ Add” link for our `Band` model, we access a form to enter details for a new band. This form incorporates validation to ensure data integrity, prompting us with errors if required fields are left blank.

2. **Read**: After creating a band, we’re redirected to a list view displaying all bands in our database. This action represents the “Read” operation, where we can visualize the data we have collected.

3. **Update**: To update an existing band, we can click on it from the list, change the details, and click “Save.” This operation modifies the existing record, showcasing the “Update” aspect of CRUD.

4. **Delete**: If we wish to remove a band, we select the band, choose “Delete selected bands” from the dropdown menu, and confirm our choice. This completes the “Delete” operation, ensuring that outdated records are removed from our database.

### Customizing the Admin Interface

The Django Admin site is primarily designed for administrators, but we can customize it to improve usability. For instance, we can enhance how the `Band` model displays in the Admin interface by modifying its string representation:

```python
class Band(models.Model):
    ...
    def __str__(self):
        return self.name
```

Additionally, we can customize the admin view by creating a `BandAdmin` class that specifies which fields to display:

```python
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')
    
admin.site.register(Band, BandAdmin)
```

With these adjustments, the Admin interface becomes more intuitive, providing clear information at a glance.

### Try It Yourself!

Now that you’re familiar with the CRUD operations in Django, it’s time to put your knowledge into practice. Register another model, such as `Listing`, in the Admin site and experiment with creating, reading, updating, and deleting records. Don’t forget to revisit and refine your existing `Band` entries, ensuring they contain accurate information.

### Conclusion

In this chapter, we learned how to perform CRUD operations through Django’s Admin site, allowing us to manage our data efficiently. This foundational skill is vital for any web application, enabling effective data manipulation and management. 

As we move forward, we’ll explore how to enhance user interactions further by creating customized forms for front-end use, ensuring a seamless experience for all users. 🚀

---

## Chapter 10: Create Many-to-One Relationships with Foreign Keys 🔗

Building on our knowledge of CRUD operations in the Django Admin, this chapter explores how to connect models together, allowing us to represent relationships in our data. Specifically, we’ll dive into **many-to-one relationships** using **Foreign Keys**.

### Understanding the One-to-Many Relationship 🎶🛍️

Imagine you’re managing merchandise listings for a band, like t-shirts or posters. Each listing belongs to one specific band, but a band can have multiple listings. This is a classic example of a **one-to-many relationship**: one band can have many listings, but each listing belongs to just one band.

For example:
- *De La Soul* might have listings for a tour poster, a t-shirt, and a concert ticket. These three listings are all related to one band—*De La Soul*. 
- But the listings can’t be tied to two bands simultaneously, like *De La Soul* and *Foo Fighters*. Each listing has only one band.

### Using Foreign Keys to Link Models 🗝️

To establish this relationship in Django, we add a **ForeignKey** field to the `Listing` model. This allows each listing to be linked to a specific band.

```python
class Listing(models.Model):
    ...
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
```

Here’s what’s happening:
- **`ForeignKey(Band)`**: This tells Django that each `Listing` is related to a `Band`.
- **`null=True`**: This allows us to create a listing even if it’s not linked to a band right away.
- **`on_delete=models.SET_NULL`**: If a band gets deleted, the `band` field in the listing will be set to `null` rather than deleting the listing.

### Updating the Database 🛠️

Once we’ve added the `ForeignKey` field, we need to update the database to reflect this change. We use the migration commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

These commands ensure our models are synchronized with the database, and we can now link bands to their listings.

### Managing Foreign Keys in the Admin Panel 🖥️

With the foreign key in place, the Django Admin panel now offers a dropdown menu when creating or editing a `Listing`. This dropdown allows us to select which band the listing is associated with.

To enhance the Admin interface, we can customize it to display the band alongside each listing:

```python
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')
```

Now, in the Admin list view, you’ll be able to see both the listing and the band it’s linked to. This makes it easier to manage and view the relationships between models.

### Conclusion

In this chapter, we’ve taken a significant step by connecting our models through **Foreign Keys**, establishing many-to-one relationships. This allows us to manage more complex data structures, making our app more dynamic and functional.

Now, each listing can be tied to a specific band, making it easier to organize and retrieve related data. 🎉

Next, we’ll explore how to improve user experience further by creating forms that allow users to interact with this connected data on the front end!

---

## Chapter 11: Overcome Common Migration Pitfalls 🚧

As we continue developing Django applications, there’s always a possibility of making mistakes while creating migrations. Don’t worry—there are two effective strategies to correct such issues:

1. **Roll Back the Migration**  
2. **Create a New Migration**

Let’s walk through each of these options.

### 1. Rolling Back an Unwanted Migration ⏪

Imagine you accidentally added a field to the wrong model and ran the migration. In this scenario, if the mistake is **only on your local machine** and hasn't been shared with other developers or pushed to production, the solution is simple—**roll it back**.

Here’s how:
- Use `python manage.py showmigrations` to view all migrations.
- Identify the unwanted migration and its predecessor.
- Run `python manage.py migrate <app_name> <previous_migration>` to roll back the specific migration.
- The migration will be undone, and you can safely delete it from your project.

### 2. Creating a New Migration 🔄

If the migration has already been shared or applied in production, rolling it back is **not an option**. Instead, you’ll need to create a new migration that undoes the unwanted changes.

To do this:
- Modify the model to remove the unwanted changes.
- Run `python manage.py makemigrations` to generate a new migration.
- Apply the new migration with `python manage.py migrate`.

This approach safely reverts the database changes, even on other machines where the initial migration has been applied.

### Handling Migration Conflicts 🔀

When working on a project with multiple developers, you may encounter **migration conflicts**—this happens when different branches add migrations with the same name. For example, two developers might add fields to the same model on different branches.

If Django detects conflicting migrations, you’ll see an error. But fear not! You can resolve this by merging the migrations using `python manage.py makemigrations --merge`. Django will combine the changes, and you can apply the merged migration.

### Conclusion 🛠️

Mistakes in migrations are common, but with the right strategies, they’re easy to fix. Whether you roll back a migration or create a new one, you can keep your database in sync and your project running smoothly. 

And when working in teams, learning to merge migrations will help you avoid conflicts and keep everyone on track. 

Happy coding! 🎉

---
## Chapter 12 : Read Data in a List View and Detail View

In this part of the Django course, the focus shifts from working behind the scenes (in the admin and shell) to crafting the user experience by building interfaces that allow users to **read** and interact with data. 

This starts with creating a **list view** and a **detail view**, essential features of any website that displays multiple objects like posts, products, or listings.

### What is a CRUD Interface? 🤔

You’ve been learning how to perform **CRUD operations** (Create, Read, Update, Delete), and now it's time to bring that power to your users. 

**They’ll be able to:**

- **Read** through lists of items (like a list of bands or listings)
- **View** details about individual items
- **Add**, **update**, or **remove** their own items

Most of the websites you use function this way! Think about social media—you create posts, edit them, and maybe even delete them. You view a list of posts (called a “feed”) and click on specific ones to see more.

### Step 1: Creating a List View 📄

The **list view** is where users see an overview of all objects in your database. For example, a list of bands, with only key details like their names displayed.

- First, you create a new template named `band_list.html` to display all band names.
- In the view (`band_list` function), you fetch all bands from the database using `Band.objects.all()`.
- You link the view to the URL path `/bands/` in `urls.py`, so when users go to that path, they see the list of bands.

Now, the page shows a simple list of band names!

### Step 2: Creating a Detail View 🔍

Next, we create the **detail view** for each band. This allows users to click on a band’s name and see more information about it, such as its genre, year formed, and a biography.

- The URL for each band's details will follow this pattern: `/bands/<id>/`, where `<id>` is the band’s unique identifier.

   ```python 
   urlpatterns = [
    ...

    # MY VIEWS
    # Model Band
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),

    ...
   
  ]
   ```
   
- The `band_detail` view retrieves a single band by its `id` using `Band.objects.get(id=id)` and passes it to the `band_detail.html` template.
- The template displays the band’s full details, including genre, year formed, and a clickable link to the band's homepage.

### Step 3: Linking the Views 🔗

It’s time to make navigation easier! Each band name in the list view will become a clickable link that takes users to the detail view for that band.

- In `band_list.html`, you wrap the band names with a link that uses Django’s `{% url %}` template tag, ensuring dynamic URLs that adapt to future changes.
   ```html
   {% extends "listings/base.html" %}

   {% block content %}
   
   <h1>Groupes</h1>
   
   <ul>
        {% for band in bands %}
            <li><a href="{% url 'band-detail' band.id %}">{{ band.name }}</a></li>
        {% endfor %}
   </ul>
   
   {% endblock %}

   ```
- You also add a “Back to all Bands” link on the detail page to guide users back to the list.

   ```html
   <p>
        <a href="{% url 'band-list' %}">Retourner a tous les groupes</a>
   </p>
   ```
Finally, to enhance navigation across the site, a **navigation bar** is added to the base template. This navbar will include a link to the list of bands and will appear on every page.

```html
<nav>
    <a href="{% url 'band-list' %}">Bands</a>
</nav>
```

### Your Turn! 🛠️

With the structure in place, it’s your task to replicate this for the **Listing** model. Build list and detail views for listings, add links between them, and ensure the site is easy to navigate with your new list and detail views.

This marks the transition from working only with backend logic to designing how users actually experience the app! 👩‍💻👨‍💻

---

## Chapter 13 : Capture User Input With Django Forms

In this chapter, you dive deeper into the "write" operations of Django by learning how to capture user input using forms and send that data from the browser to the server.

### What are Forms? 🤔
Forms allow users to input data, like creating a new band, and send it to the server. Unlike "read-only" operations, forms handle "write" operations, which modify data in some way. You'll encounter forms when users need to create, update, or delete data.

In this chapter, you explore how to build a “Contact Us” form, starting by defining the form itself.

### Define a Form in Django ✍️
You begin by creating the form class, just like you create models. Each form field represents an input the user will fill in, such as name, email, and message. 

In Django, you can easily set constraints like optional fields (`required=False`) or max character limits.

```python
class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
```

This form is integrated into your view, and Django renders it for you with just one line of code: `{{ form }}`.

### Handle Form Data in Views 📥
Once users submit the form, Django sends the data to the server as an HTTP POST request. The view now handles two scenarios:

1. **GET Request:** Shows the form for the user to fill out.
2. **POST Request:** Receives and processes the form data.

By using simple print statements, you can inspect the data received from the form.

```python
if request.method == 'POST':
    form = ContactUsForm(request.POST)
    if form.is_valid():
        # send the email
else:
    form = ContactUsForm()
```

### Server-Side Validation ✔️
Django automatically validates the input based on the form rules you’ve defined. If the data is invalid, the form reloads with helpful error messages, giving the user a chance to correct it.

This cycle ensures clean, correct data before proceeding to send an email.

### Send an Email ✉️
If the form is valid, Django sends an email using the `send_mail` function. The email details, like subject and body, are pulled from the cleaned form data. 

```python
# views.py

send_mail(
    subject=f'Message from {form.cleaned_data["name"] or "anonymous"}',
    message=form.cleaned_data['message'],
    from_email=form.cleaned_data['email'],
    recipient_list=['admin@example.com']
)
```
To test this, Django can print email contents to the terminal instead of sending a real email by configuring the console email backend.

```python
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Redirect After POST ➡️
To avoid duplicate form submissions (like accidentally sending the same message twice), you implement a redirect. After the form submission, instead of reloading the same page, Django redirects users to a confirmation page.

```python
from django.shortcuts import redirect

...

return redirect('email-sent')
```

This small improvement not only enhances user experience but also prevents repeated actions like multiple email submissions.

By the end of this chapter, you've learned how to capture user input, process it on the server, validate it, and finally perform an action like sending an email. 😎

---

Let's dive into this section with a technical storytelling approach!

---

## Chapter 14 : Creating Bands with ModelForms 🎸🎤

Now that we're ready to start adding bands to our app, we’ll use Django’s **ModelForm** to make it easy to create new bands.

First, let’s think about the **URL**. 

Up until now, we've used paths like `/bands/` for the band list and `/bands/1/` for specific bands. For creating new bands, how about we use `/bands/add/`? 

We place this pattern under the rest of the band's URLs in our `urls.py`:

```python
urlpatterns = [
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
]
```
The beauty of Django’s routing is that we can use any verb we want, as long as it makes sense to users.

### Letting the Model Shape the Form ✍️

Instead of manually defining each form field, Django offers **ModelForms** that can generate forms automatically based on your model. 

In our case, the `BandForm` will inherit from `ModelForm`, and Django will handle the rest! Here’s the code:

```python
class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
```
This means the form will automatically include all fields from the `Band` model. If we ever update the model, the form will adjust accordingly! No need to rewrite the form each time the model changes—how convenient is that? 😎

### View Logic: Handling POST and GET Requests 💻

Next, let’s update the view logic to handle creating a new **Band** object. The `band_create` view will check whether the request is a **GET** (to show an empty form) or a **POST** (to process the submitted form). 

If the form passes validation, we create the band and redirect the user:

```python
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})
```
This pattern ensures that we handle both the initial form display and the subsequent form submission properly.

### Enhancing User Experience with Client-Side Validation 🌐

By default, Django provides **server-side validation** to ensure that data is valid before saving it to the database. But it’s also a good idea to enable **client-side validation** for a smoother user experience. 

Removing the `novalidate` attribute from the form allows the browser to check for issues before the form is submitted.

However, client-side validation isn't enough on its own. Users could tamper with the HTML to bypass it, so **server-side validation** is still crucial. 

In web development, there’s a golden rule: “Never trust the client!” 🚨

### Keeping Your Forms Secure 🔒

If you’ve noticed the `{% csrf_token %}` in our forms, it’s there for a reason! This token protects your app from **cross-site request forgery (CSRF)** attacks by ensuring that only legitimate requests are processed.

By the end of this chapter, you've learned how to generate forms from models with minimal effort, making your code more efficient and secure. Now, you’re ready to create new bands, validate forms, and make your app more user-friendly! 🎉

---

## Chapter 15 : Update a Model Object With a ModelForm

In this chapter, we learn how to **update model objects using ModelForm** in Django. The journey begins by adding a **URL pattern**, **view**, and **template** for updating a specific band in our database.

### Setting Up the URL Pattern
We’ve already set up URLs for listing bands (`bands/`), viewing individual bands (`bands/1/`, `bands/2/`, etc.), and adding new bands (`bands/add/`). 

Now, we need a URL for updating a band. For this, we choose `bands/<id>/change/`, where `<id>` represents the band’s ID. This URL makes it clear that we are modifying an existing band.

### Creating the View and Template
In our view, we handle both GET and POST requests. When a user first accesses the page, a form is displayed, **pre-filled with the band's existing data**. 

This is done using Django’s `instance` parameter in the form, like this:

```python
form = BandForm(instance=band)
```

Next, we need to add logic to handle the POST request when the form is submitted. If the form is valid, we save the updated data to the database and then **redirect** the user to the band’s detail page.

### Reusing the ModelForm
The beauty of Django’s forms is that we can reuse the same form for both creating and updating records. In this case, we don’t need to create a new form for updating a band. 

By passing the `instance=band` argument, we can pre-populate the form with the band's current data, and then update it with any changes.

### Linking to the Update Page
We provide links to the update page from two places: 
1. The **band list page**, where each band has an "edit" link next to it.
2. The **band detail page**, where a more prominent "Edit this Band" link is available at the bottom.

These small links guide users seamlessly into editing any band, ensuring an easy and intuitive user experience. 🎸

### Conclusion
With this chapter, you’ve learned how to set up an update view for Django models, **reuse forms**, and link the update functionality to your templates. 

Now, your users can not only create but also update band records in a user-friendly way! 🎶

---

## Chapter 16 : Delete Objects Safely With User Confirmation

In this chapter, we dive into the process of **deleting objects safely** in Django, ensuring users don't accidentally remove important data. 🛡️

### Step 1: Confirm Before Deleting
Deleting an object in a database is irreversible, so it's important to give users a chance to **change their minds**. To do this, Django uses a two-step process:
1. **Delete button**: Clicking it doesn’t immediately delete the object; instead, it leads to a **confirmation page**.
2. **Confirmation page**: Here, the user must choose between "Yes, I'm sure" or "No, take me back," ensuring the delete action is intentional.

### Step 2: Add a URL Pattern and View for Delete Confirmation
We need to create a new view and URL pattern for the confirmation page. Following the established URL structure, the path will look like `bands/1/delete/` for deleting band 1.

In the view, we pass the band object to the template, allowing us to display the band’s name and confirm which object is being deleted:

```python
def band_delete(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_delete.html', {'band': band})
```

### Step 3: Simple Delete Form
On the confirmation page, we show a **basic form** with just a submit button to finalize the deletion:

```html
<form action="" method="post">
    {% csrf_token %}
    <input type="submit" value="Delete">
</form>
```

Since the band’s ID is already in the URL, there's no need to pass any additional data. Once the form is submitted, the server knows which band to delete by checking the URL.

### Step 4: Handling the Deletion in the View
In the view, we check if the request is a **POST** (indicating the user confirmed the deletion). If it is, we call `band.delete()` to remove the object from the database, and then redirect the user to the band list:

```python
if request.method == 'POST':
    band.delete()
    return redirect('band_list')
```

### Step 5: Redirect and Flash Messages
After the band is deleted, the user is redirected to the list of bands, where the deleted band is no longer shown. To enhance the user experience, you might want to display a **flash message** confirming the deletion, just like Django’s admin interface does. 

Flash messages can provide immediate feedback, helping users understand their actions were successful. 💡

### Conclusion
This chapter walks you through the process of safely deleting objects in Django, using confirmation pages to prevent accidental deletions. Users can now confidently manage their data, knowing they have a chance to review their decision before it's final. 🗑️

---

# Intermediate Django @2024

---

## Chapter 1 : Intro

### Learn From a Professional Scenario

In this course, you will create a full web application from start to finish - the context is outlined below:

A photography collective is looking for a way to share its work with the world. They want to be able to upload their photos online and also create blog posts about them. 

They have asked you, a Django developer, to build a web application that allows them to do just that. They need to have two tiers of users - subscribers and creators - and ensure that only the creators can create content. 

This content then needs to be shared in a social feed, with subscribers choosing which creators they want to follow.

---

Here's the summary in a storytelling style with emojis as requested:

---

## Chapter 2 : Customize the User Model in Django 🎨

Before we jump into customizing user authentication in Django, let's first set up the project and environment. 🎬

### 1. **Project Setup 🛠️**
We begin by creating a project directory for a photo-sharing blog named **fotoblog**. Then, we set up the Python virtual environment, install Django, and create two apps:
- **authentication** for managing users.
- **blog** for handling posts and photo-sharing.

After setting up the environment and installing necessary packages, we make our initial Git commit and are ready to move forward. 💻

### 2. **Exploring Django's User Model 🧑‍💻**
By default, Django provides a built-in `User` model for managing user data such as usernames, emails, and passwords. 

This model is feature-rich, with fields for:

- **Username**, **First Name**, **Last Name**, **Email**, and **Password** (stored securely as a hash 🔒).
- User status fields like **is_active**, **is_staff**, and **is_superuser**.

However, these fields may not always match your needs, which is where customization comes in! 😎

### 3. **Customizing the User Model 👩‍🎨**
Even if you don't plan to change the default `User` model immediately, it's a best practice to implement a custom user model from the start. This prevents future migration headaches if your project grows in complexity. 

Django provides two base classes you can use to create your custom user models:

- **AbstractUser**: Keeps all fields of the default `User` model but allows you to add custom fields.
- **AbstractBaseUser**: Strips down to the basics, providing just authentication-related fields, giving you full flexibility to design the model from scratch.

#### Example: Adding an Account Number 🧾
You can easily add fields like an account number by extending `AbstractUser`. For instance:

```python
class User(AbstractUser):
    account_number = CharField(max_length=10, unique=True)
```

Or, if you don't need some fields (like `username`), you can customize the model with `AbstractBaseUser` for full control.

### 4. **Creating a Custom User Model for Our App 📸**
In our **fotoblog** app, we want to allow users to upload a profile photo and define their role (creator or subscriber). 

We extend `AbstractUser` to add these fields:

```python
class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    class Role(models.TextChoices):
        CREATOR = 'CREATOR'
        SUBSCRIBER = 'SUBSCRIBER'

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=Role.choices)
```

### 5. **Configuring Django to Use the Custom User Model 🔧**
Next, we tell Django to use our custom `User` model by setting the `AUTH_USER_MODEL` in `settings.py`:

```python
AUTH_USER_MODEL = 'authentication.User'
```

### 6. **Running Migrations 🏃‍♂️**
Before migrating, we install **[Pillow](https://pypi.org/project/pillow/)** to handle the `ImageField` for user profile photos. After that, we create and run migrations, finalizing the setup.

Now, the custom user model is fully integrated into Django, ready to manage authentication with ease! 🎉

---

## Chapter 3: Create a Login Page with Function-Based Views 🔐

Now that we’ve customized the User model to fit the needs of our **fotoblog** app, the next step is enabling users to log in to their accounts. This chapter guides you through creating a login page using Django's function-based views.

### 1. **Understanding Function-Based Views (FBVs) 🧑‍💻**

Function-based views in Django allow you to handle web requests with simple Python functions. For our login page, we will build an FBV to manage both GET and POST requests.

The GET request will display the login form, while the POST request will process the submitted data to authenticate the user.

### 2. **Building the Login Form 📝**

We start by creating a `LoginForm` class in `forms.py`. This form will capture the username and password from users. To keep passwords secure, we use Django’s `PasswordInput` widget to mask the input field.

Example of the form:
```python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
```

### 3. **Creating the Login View 📲**
In `views.py`, we define the `login_view` function. This function will handle both displaying the form and processing the submitted data. 

Django's built-in `authenticate` function checks if the provided credentials are correct, and `login` logs the user in.

Here’s how the view is structured:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
            else:
                error_message = 'Invalid credentials'
        else:
            error_message = 'Form is not valid'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
```

### 4. **Designing the Login Template 🎨**
The login page is created as `login.html` in the templates directory. This template extends the base template and contains the login form. 

Additionally, it includes CSRF protection to ensure secure communication between the client and server.

Basic structure of the login template:

```html
{% extends "base.html" %}

{% block content %}
  <h2>Login</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
  </form>
  {% if error_message %}
    <p style="color:red;">{{ error_message }}</p>
  {% endif %}
{% endblock %}
```

### 5. **Mapping the Login View to a URL 🌐**
To make the login page accessible, we define a URL pattern in `urls.py`:

```python
from django.urls import path
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
]
```

### 6. **Testing and Adding Logout 🧪**
Once the login system is set up, you can test it by creating a test user using the Django shell. After logging in successfully, you’ll want to add a logout option. 

This can be easily implemented by using Django’s built-in `logout` function.

```python
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect back to the login page after logging out
```

### 7. **Restricting Pages to Logged-In Users Only 🔒**
To restrict access to certain pages for authenticated users only, Django provides the `login_required` decorator. This ensures that users must be logged in before accessing those views.

Example:
```python
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home.html')
```

### 8. **Conclusion 🏁**
With the login system fully implemented, users can now securely log into their accounts on **fotoblog**. This login system not only handles authentication but also redirects users to the appropriate pages based on their login status. 

In the next chapter, we will explore how to enhance user sessions and add additional security features! 🎉

---

## Chapter 4: Create a Login Page With Class-Based Views 🏗️

After setting up the login page using function-based views (FBVs), it's time to explore a more structured and flexible approach—**class-based views (CBVs)**. 

This chapter will guide you through `refactoring` the previous login system into a class-based structure, offering better organization and maintainability. 🌟

### 1. **Introduction to Class-Based Views (CBVs) 🤔**
Class-based views allow us to represent views as classes rather than functions. Unlike FBVs that handle different HTTP methods in a single function, CBVs split this logic across separate methods like `get` and `post`. 

This makes the code easier to maintain and extend over time. 💡

### 2. **Refactoring the Login View to a Class-Based View 🔄**
In this step, we will convert the `login_view` FBV into a class-based view, `LoginPageView`. 

The logic remains the same, but the structure is more modular:

- **GET method**: Handles displaying the login form.
- **POST method**: Handles form submission and user authentication.

Here’s the new class-based view:
```python
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

class LoginPageView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            error_message = 'Invalid credentials'
        return render(request, self.template_name, {'form': form, 'error_message': error_message})
```
In this version, the `get` and `post` methods handle requests separately, providing cleaner, more organized code. 🎯

### 3. **Adding the URL Pattern 🔗**
To use the class-based view in Django, we need to update the URL configuration by calling `as_view()` on the class.

```python
from django.urls import path
from .views import LoginPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
]
```
This `as_view()` method converts the class into a view that Django can recognize. 🚀

### 4. **Why Class-Based Views? 🤷**
The advantage of using CBVs is the ability to reuse and extend the class easily. For instance, we can change templates or form logic by subclassing the `LoginPageView`. 

CBVs offer greater flexibility and scalability for larger projects. 🏗️

### 5. **Leveraging Generic Views for Authentication ⚙️**
Django offers generic views, which further simplify common tasks like authentication. Instead of writing custom login logic, you can use the built-in `LoginView`. 

This allows you to focus on customizing the interface while letting Django handle the backend logic.

Example:
```python
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]
```
Using generic views reduces repetitive code, providing a cleaner and faster implementation. 💼

### 6. **Conclusion 🏁**
By refactoring the login page into a class-based view, we’ve created a more modular and maintainable authentication system. This structure will be easier to extend and scale as the project grows. 

Now that we have implemented the authentication views, let's build the site's signup functionality.

---

## Chapter 5: Create a Sign-Up Page 📝

After establishing a structured login system using class-based views (CBVs), the next logical step is to implement user registration. 

In this chapter, we will create a **sign-up page**, allowing users to register and create their accounts. Like the login process, we'll leverage Django’s built-in tools and customize them to fit our specific needs. 

### 1. **Extending the UserCreationForm ✍️**

Django provides a pre-built **UserCreationForm** that simplifies user registration by managing common fields like `username` and `password`. However, in many applications, additional fields such as `email`, `first_name`, or `role` are necessary. 

To accommodate this, we’ll extend the `UserCreationForm` by adding these fields.

Here’s a custom form example:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

This custom form now includes an email field, allowing us to gather more user data upon registration.

### 2. **Creating the Sign-Up View 👤**

With the form ready, we need a view to handle user registration. We’ll create a class-based view, `SignUpView`, to process user input, validate the form, and save new users to the database.

Here’s the class-based view:

```python
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

class SignUpView(View):
    template_name = 'authentication/signup.html'
    form_class = CustomUserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
```

This view handles both **GET** requests (displaying the empty form) and **POST** requests (processing form data and creating a new user).

### 3. **Creating the Sign-Up Template 🎨**

The next step is to design the user interface for the sign-up page. We’ll create a simple HTML template to display the form, ensuring it follows the same styling as the login page for consistency.

Here’s a sample template (`signup.html`):

```html
<h2>Sign Up</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
```

This form includes CSRF protection and uses Django’s built-in form rendering with `as_p` for simple layout.

### 4. **Adding the Sign-Up URL 🌐**

We must now add a URL pattern for the sign-up page to make it accessible to users. In the `urls.py` file, we define a route for the `SignUpView`.

```python
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
```

This ensures that users can visit `/signup/` to access the registration page.

### 5. **Handling Password Validation and Security 🔐**

To ensure strong password policies, Django includes built-in password validators. These can be customized in the settings file to require a combination of letters, numbers, and special characters. 

Password security is critical for protecting user accounts, so enabling these validators is highly recommended.

Example of a password validator configuration:

```python
# authentication/validators.py
from django.core.exceptions import ValidationError

class ContainsNumberValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'The password must contain a number',
                code='password_no_numbers'
            )

    def get_help_text(self):
        return 'Your password must contain at least one number.'
```

```python
# photoblog/settings.py

AUTH_PASSWORD_VALIDATORS = [
   
   # DJANGO DEFAULT VALIDATORS
   {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
   {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
   
   # CUSTOM VALIDATORS
   {
      'NAME': 'authentication.validators.ContainsNumberValidator',
   },
]
```

### 6. **Next Steps: Email Verification and More Advanced Features 📧**

While the basic sign-up process is now in place, we can further improve the user experience and security by adding features like **email verification**. 

Django provides **[third-party packages](https://djangopackages.org/)** for handling email confirmation, which ensures that users provide a valid email address during registration. 

Additionally, you could integrate **[social media logins](https://medium.com/@michal.drozdze/django-rest-framework-jwt-authentication-social-login-login-with-google-8911332f1008)** to simplify the process for users by allowing them to register with their existing accounts from platforms like Google or Facebook.

### 7. **Conclusion 🏁**

In this chapter, we built a **sign-up page** using Django’s **UserCreationForm** and class-based views, making it easy for users to register for an account. 

This flexible approach will enable future enhancements like email verification and password strength enforcement.

--- 

## Chapter 6: Add an Image Upload Facility to Your Blog 🖼️

Now that users can create accounts through the sign-up page, it's time to allow them to enhance their blog posts with images. 

In this chapter, we’ll implement an **image upload feature**, enabling users to attach photos to their blog entries and personalize their content.

### 1. **Defining the Photo Model 📷**

We’ll begin by creating a model to store information about the uploaded images. This includes fields for the image file and a caption to describe the photo.

Here’s the `Photo` model:

```python
from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption if self.caption else 'No Caption'
```

This model uses Django's **ImageField** to handle image uploads and connects each photo to a user via a `ForeignKey`. The `upload_to` argument ensures that uploaded files are stored in a specific directory within your project.

### 2. **Configuring Media Settings 🛠️**

To manage media files like images, you need to configure Django to handle uploads properly. We do this by defining the `MEDIA_URL` and `MEDIA_ROOT` in the **settings.py** file.

```python
# photoblog/settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media/')
```

These settings tell Django where to store uploaded files and how to make them accessible during development.

### 3. **Creating a Photo Upload Form 📝**

Next, we’ll create a form that users can use to upload their images. This form is built using Django's `ModelForm`, which automatically generates fields based on the `Photo` model.

```python
from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']
```

With this form, users can select an image from their device and add a caption before submitting the form.

### 4. **Building the Photo Upload View 📥**

We’ll create a view to handle the upload form. This view will manage both GET and POST requests, displaying the form and processing the uploaded image.

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('profile')
    else:
        form = PhotoForm()
    return render(request, 'blog/upload_photo.html', {'form': form})
```

This view ensures that only logged-in users can upload photos, and it saves the image and caption to the database.

### 5. **Creating the Upload Template 🎨**

We’ll now design a simple HTML template to display the photo upload form.

```html
<h2>Upload a Photo</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

The form includes the `enctype="multipart/form-data"` attribute to handle file uploads properly.

### 6. **Adding the URL Pattern 🌐**

Finally, we’ll add a URL pattern for the photo upload view to make it accessible to users.

```python
# blog/urls.py
from django.urls import path
from .views import upload_photo

urlpatterns = [
    path('upload/', upload_photo, name='upload_photo'),
]
```

Now users can visit `/upload/` to access the photo upload page.

### 7. **Displaying Uploaded Photos 🖼️**

Once users have uploaded photos, we need to display them. This can be done by fetching the uploaded images and displaying them in the user’s profile or blog feed.

```html
<h2>{{ user.username }}'s Photos</h2>
<ul>
    {% for photo in user.photo_set.all %}
    <li>
        <img src="{{ photo.image.url }}" alt="{{ photo.caption }}">
        <p>{{ photo.caption }}</p>
    </li>
    {% endfor %}
</ul>
```

This template loops through the user’s uploaded photos and displays each image along with its caption.

### 8. **Next Steps: Adding Profile Pictures 👤**

Now that users can upload photos for their blog posts, the next step could be to add profile pictures for each user. This enhances personalization and improves user engagement on the platform.

### 9. **Conclusion 🏁**

In this chapter, we implemented an image upload feature using Django's **ImageField** and **ModelForm**, allowing users to attach photos to their blog posts. This functionality will make the blog more dynamic and visually engaging.

---

## Chapter 7: Add a Blog Post Creation Facility 📝

After enabling users to upload images, the next step is allowing them to create blog posts. In this chapter, we’ll integrate a **blog post creation feature**, where users can write posts, upload images, and enhance their content seamlessly.

### 1. **Define the Blog Post Model 🖋️**

We’ll begin by creating a `Blog` model to store the content of each blog post. This model will include fields for the title, content, and an optional photo that can be attached to each post.

```python
from django.db import models
from .models import Photo
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Here, the `photo` field is optional, allowing users to create blog posts with or without an image.

### 2. **Create Blog and Photo Forms 📝**

Next, we need forms for both the `Blog` and `Photo` models to handle the user inputs. We already have a `PhotoForm`, so we’ll create a `BlogForm` that gathers the post’s title and content.

```python
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
```

### 3. **Build the Blog Creation View 💻**

We’ll now create a view that handles both the `BlogForm` and `PhotoForm` together. This view will ensure that users can upload a photo and write a blog post in one step.

```python
from django.shortcuts import render, redirect
from .forms import BlogForm, PhotoForm

def create_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if blog_form.is_valid() and photo_form.is_valid():
            photo = photo_form.save(commit=False)
            photo.user = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('blog_list')
    else:
        blog_form = BlogForm()
        photo_form = PhotoForm()
    return render(request, 'blog/create_blog.html', {'blog_form': blog_form, 'photo_form': photo_form})
```

### 4. **Create the Blog Creation Template 🎨**

We’ll create a template that includes both forms, allowing users to write blog posts and upload images simultaneously.

```html
<h2>Create a Blog Post</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ blog_form.as_p }}
    {{ photo_form.as_p }}
    <button type="submit">Create Blog Post</button>
</form>
```

### 5. **Add the URL Pattern 🌐**

Finally, we add a URL pattern to link the view to the blog creation page.

```python
path('blog/create/', create_blog, name='create_blog'),
```

### 6. **Display Blog Posts 🖼️**

Once users create blog posts, we need to display them. We can create a view to list all the blog posts and their attached images.

```html
<h2>Recent Blog Posts</h2>
<ul>
    {% for blog in blogs %}
    <li>
        <h3>{{ blog.title }}</h3>
        <p>{{ blog.content }}</p>
        {% if blog.photo %}
        <img src="{{ blog.photo.image.url }}" alt="{{ blog.photo.caption }}">
        {% endif %}
    </li>
    {% endfor %}
</ul>
```

### 7. **Conclusion 🏁**

In this chapter, we added a **blog post creation feature** that allows users to write posts, upload photos, and personalize their content. 

This addition makes the blog platform more interactive and user-friendly, providing a space for users to express their thoughts and showcase their images.

---

## Chapter 8: Include Multiple Forms on the Same Page 📝

Building on the blog post creation facility, the next step is enhancing user interactions by allowing them to **manage multiple forms** on the same page. 

In this chapter, we’ll explore how users can edit or delete a blog post simultaneously, providing a more seamless experience.

### 1. **Defining Multiple Forms 🖋️**

We'll start by defining two forms for handling different tasks on the same page:

- **BlogForm**: To allow users to **edit** their blog posts.
- **DeleteBlogForm**: To enable users to **delete** a blog post.

By creating these forms, we give users the ability to manage their posts without leaving the current page.

```python
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    edit_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Blog
        fields = ['title', 'content']


class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
```

### 2. **Handling Multiple Forms in the View 👨‍💻**

To process both forms on the same page, we modify the `edit_blog` view. The view will:

- Handle the **edit** form to save changes to a blog post.
- Process the **delete** form when a user confirms deletion.

This logic ensures that each form works independently, yet harmoniously, on the same page.

```python
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            blog_form = BlogForm(request.POST, instance=blog)
            if blog_form.is_valid():
                blog_form.save()
                return redirect('blog_detail', pk=blog.pk)
        elif 'delete_blog' in request.POST:
            delete_form = DeleteBlogForm(request.POST)
            if delete_form.is_valid() and delete_form.cleaned_data['confirm']:
                blog.delete()
                return redirect('blog_list')
    else:
        blog_form = BlogForm(instance=blog)
        delete_form = DeleteBlogForm()

    return render(request, 'blog/edit_blog.html', {
        'blog_form': blog_form,
        'delete_form': delete_form,
        'blog': blog
    })
```

### 3. **Designing the Template 🎨**

In the template, both forms are displayed together, each with its own submit button. This layout allows users to either **edit** or **delete** their blog post on the same page.

```html
<h2>Edit Blog Post</h2>
<form method="post">
    {% csrf_token %}
    {{ blog_form.as_p }}
    <button type="submit" name="edit_blog">Save Changes</button>
</form>

<h2>Delete Blog Post</h2>
<form method="post">
    {% csrf_token %}
    {{ delete_form.as_p }}
    <button type="submit" name="delete_blog">Delete Blog Post</button>
</form>
```

### 4. **Using Formsets for Multiple Instances 📸**

If the page involves repeating the same task, such as **uploading multiple photos**, we can use Django’s `formset_factory` to manage several forms simultaneously.

```python
from django.forms import modelformset_factory
from .models import Photo

...

PhotoFormSet = modelformset_factory(Photo, fields=('image', 'caption'), extra=3)
formset = PhotoFormSet()

...
```

### 5. **Template for Multiple Uploads 🎨**

We modify the template to include multiple photo upload fields, using a formset to handle the inputs.

```html
<h2>Upload Photos</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ formset.management_form }}
    {% for form in formset %}
        {{ form.as_p }}
    {% endfor %}
    <button type="submit">Upload Photos</button>
</form>
```

### 6. **Conclusion 🏁**

In this chapter, we explored how to include and handle **multiple forms on the same page**, whether for editing, deleting, or uploading multiple items. 

This feature enhances user experience by allowing more control over managing their content in a streamlined way.

---

## Chapter 9: Manipulate Models by Overriding Model Methods 🔧

Building on the ability to manage multiple forms on a single page, we now dive into a deeper level of customization with **model manipulation**. 

In this chapter, you'll learn how to **override model methods** to automate tasks and keep your views even more efficient.

### 1. **Fat Models, Skinny Views 💪**

The Django philosophy of **fat models, skinny views** suggests that the **heavy logic** should live in the model, while the views handle minimal tasks. This approach makes your views cleaner and your logic reusable.

In this case, we need to **resize images** when users upload photos. Instead of doing this in the view, we’ll add the logic to the **Photo model** itself, making it more efficient and allowing it to be reused wherever needed.

### 2. **Resizing Images Automatically 📷**

We’ll create a custom method in the `Photo` model called `resize_image()` to handle resizing photos before they’re saved. This helps reduce storage space as the number of uploaded images grows.

```python
from PIL import Image


class Photo(models.Model):

    # Images treatments
    IMAGE_MAX_SIZE = (800, 800)

    # Fields
    image = models.ImageField()
    
    ...
    
    def __str__(self):
        return self.caption

    def resize_image(self):
        image = Image.open(self.image.path)
        image.thumbnail(self.IMAGE_MAX_SIZE)

        # save teh resized image to the file system
        image.save(self.image.path)
```

By using the **Pillow** library, we can resize images to fit a specified maximum size while maintaining the aspect ratio. The logic is placed in the model method, so it doesn't clutter up the views.

### 3. **Overriding the `save()` Method 🤖**

Manually calling `resize_image()` every time a photo is uploaded isn’t practical. Instead, we **override the `save()` method** in the `Photo` model. 

This ensures that every time a new photo is uploaded, it is automatically resized before being saved to the database.

The **super()** function is used to ensure the original save process runs correctly, while the resized image is handled afterward.

```python
class Photo(models.Model):
    ...

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
```

This small change simplifies image handling, making the process fully automatic. The method is reusable and can be applied anytime the `save()` method is called.

### 4. **Customizing the Blog Model 📝**

We extend this concept to the **Blog model**, adding a feature to calculate the **word count** of blog posts. Instead of calculating it each time on the fly, we store it in a field (`word_count`), and update it every time the blog content is saved.

```python

class Blog(models.Model):
    ...
    content = models.CharField(max_length=5000)
    ...
    
    word_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def _get_word_count(self):
        word_count = len(self.content.split(' '))

        return word_count

    def save(self, *args, **kwargs):
        # compute word count
        self.word_count = self._get_word_count()

        # save
        super().save(*args, **kwargs)
```

By creating a custom `_get_word_count()` method and overriding the `save()` method, we ensure the word count stays accurate and up-to-date.

### 5. **Key Takeaways 📌**

- Use **fat models** to keep your views clean by placing logic in **model methods**.
- **Override model methods** like `save()` to automate repetitive tasks, such as resizing images or updating fields.
- This approach makes your code more **reusable** and easier to maintain.

With these techniques, you can take control of your data and streamline processes in your Django apps, keeping your views simple and efficient.

---

## Chapter 10: Assign Permissions Using Groups

Here's a recap of the key points with code snippets to make it clearer how you can implement permissions using groups in Django:

### 1. Restricting Site Access Using Permissions 🚪🔐

Imagine your website has two types of users: Creators and Subscribers. Creators need to create, edit, and delete photos and blog posts, while subscribers should only be able to view content. 

To manage this, we rely on Django's built-in permission system. For every model you create, Django automatically generates four permissions:

- **Add:** Permission to add new entries
- **Change:** Permission to modify entries
- **Delete:** Permission to remove entries
- **View:** Permission to access entries

Django uses these permissions in the admin interface, but you can integrate them into your site's logic.

To restrict access to a view, use the `@permission_required` decorator. This ensures only users with the correct permission can access certain views.

```python
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

@login_required
@permission_required('blog.add_photo', raise_exception=True)
def photo_upload(request):
    # Logic for handling photo upload
    return render(request, 'blog/photo_upload.html')
```
In this example, only users with the `blog.add_photo` permission can access the **photo upload** view.

### 2. Restricting Access in Templates 👁️‍🗨️

You can hide or display elements in your templates based on the user’s permissions using the `perms` context variable.

```html
<!-- Only show the upload button to users with the 'add_photo' permission -->
{% if perms.blog.add_photo %}
    <a href="{% url 'photo_upload' %}">Upload a Photo</a>
{% endif %}
```
This checks if the user has the `add_photo` permission and, if so, shows the **Upload Photo** link.

### 3. Granting Permissions to a User 🛠️

Assign permissions to users programmatically (in the `django shell`), like this:

```python
from django.contrib.auth.models import User, Permission

# Get the user and permission
user = User.objects.get(username='johnsmith')
permission = Permission.objects.get(codename='add_photo')

# Add permission to the user
user.user_permissions.add(permission)

# Save changes
user.save()
```

This adds the `add_photo` permission to the `johnsmith` user.

### 4. Organizing Users with Groups 📚

Groups are a great way to manage permissions for multiple users. First, create a custom migration to create groups and assign permissions.

#### Step 1: Create a Custom Migration

```bash
python manage.py makemigrations --empty authentication
```

#### Step 2: Define Groups and Permissions in the Migration

```python
from django.db import migrations

def create_groups(apps, schema_editor):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Get permissions
    add_photo = Permission.objects.get(codename='add_photo')
    view_photo = Permission.objects.get(codename='view_photo')

    # Create Creator group and assign permissions
    creators = Group(name='creators')
    creators.save()
    creators.permissions.add(add_photo, view_photo)

    # Create Subscriber group
    subscribers = Group(name='subscribers')
    subscribers.save()
    subscribers.permissions.add(view_photo)

    # Assign users to the appropriate group
    for user in User.objects.all():
        if user.role == 'CREATOR':
            creators.user_set.add(user)
        elif user.role == 'SUBSCRIBER':
            subscribers.user_set.add(user)

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
```
This migration creates two groups: **creators** and **subscribers**. Creators get the `add_photo` and `view_photo` permissions, while subscribers only get the `view_photo` permission.

### 5. Adding Custom Permissions 🎛️

If you need custom permissions, you can define them in the `Meta` class of your model.

```python
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
            ('change_blog_title', 'Can change the title of a blog')
        ]
```

With this custom permission, you can now control access to the blog title field in your views or templates.

---

## Chapter 11: Create Many-to-Many Relationships with Foreign Keys

Now that you have a solid understanding of managing permissions using groups in Django, it’s time to explore how to connect different models using **Many-to-Many Relationships**. 

This feature allows you to link multiple records from one model to multiple records in another, enhancing the flexibility of your application's database structure.

### 1. Understanding Many-to-Many Relationships 🔗

In the previous chapters, you learned how to set up **ForeignKey** fields to create one-to-many relationships, such as linking a photo to a single user. However, some situations call for a more complex relationship. 

For example:

- **Users** can follow multiple **creators**, and a **creator** can be followed by multiple users.
- **Blog posts** can have multiple **contributors**, and **contributors** can contribute to multiple **blogs**.

This is where **Many-to-Many** relationships come in. Django simplifies this with the **ManyToManyField**.

### 2. Implementing a Many-to-Many Field 🔨

Let’s start by adding a **ManyToManyField** to the `User` model, allowing users to follow creators. Here's how to define this relationship:

```python
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.user.username
```

In this setup:
- `following`: A user can follow many other users.
- `followers`: This `related_name` allows you to access the followers of a user easily.

### 3. Creating the Form and View ✍️

You’ll need to create a form that lets users select which creators to follow. Use a **ModelForm** for this:

```python
from django import forms
from django.contrib.auth import get_user_model

# models
User = get_user_model()

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['following']
```

Then, create a view to handle the form submission:

```python
from django.shortcuts import render, redirect
from .forms import FollowForm
from django.contrib.auth.decorators import login_required

@login_required
def follow_users(request):
    if request.method == 'POST':
        form = FollowForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = FollowForm(instance=request.user.userprofile)
    
    return render(request, 'follow_users.html', {'form': form})
```

This view ensures only logged-in users can follow others, and the **ModelForm** handles saving the many-to-many relationships.

### 4. Displaying Many-to-Many Data in Templates 📜

Once users start following each other, you might want to display the data in your templates. For instance, show which creators a user follows:

```html
{% if user.role == user.CREATOR %}
     <h3>Followers</h3>
     <ul>
         {% for follower_user in user.user_set.all %}
             <li>{{ follower_user.username }}</li>
         {% endfor %}
     </ul>
 {% endif %}

 {% if user.role == user.SUBSCRIBER %}
     <h3>Following</h3>
     <ul>
         {% for following_user in user.followers.all %}
             <li>{{ following_user.username }}</li>
         {% endfor %}
     </ul>
 {% endif %}
```

This template snippet loops through the `followers` field and lists the creators a user follows.

### 5. Storing Extra Data with Intermediary Tables 🗄️

Sometimes, you need to store additional information about the relationship itself. For example, you might want to keep track of **contributors** to a blog post and specify what each contributor has added. 

Django allows this with **intermediary models**.

#### Step 1: Define the Intermediary Model

First, create an intermediary model to store the extra data:

```python
class Contribution(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255)
```

#### Step 2: Update the Blog Model

Next, link this intermediary model to the **Blog** model using the **ManyToManyField** with the `through` attribute:

```python
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    contributors = models.ManyToManyField(User, through='Contribution')
```

#### Step 3: Saving the Data

In your view, you can now save both the blog and the contributions:

```python
from .models import Blog, Contribution

def blog_and_photo_upload(request):
    if request.method == 'POST':
        # Save blog
        blog = Blog.objects.create(title=request.POST['title'], content=request.POST['content'])
        
        # Add contributors
        Contribution.objects.create(blog=blog, user=request.user, contribution='Main content')
        return redirect('blog_list')
```

### 6. Migration Strategy: From ForeignKey to Many-to-Many ⚙️

If you started with a **ForeignKey** and now need to migrate to a **ManyToManyField**, you'll need to:
- Create a new **ManyToManyField**.
- Write a migration script to transfer existing relationships into the many-to-many table.
- Remove the original **ForeignKey** after verifying the migration is successful.

By the end of this chapter, you've learned how to link models in Django with **Many-to-Many relationships** and handle extra data using intermediary tables. 

This provides a more dynamic way to manage relationships between models, especially when dealing with complex applications.

---

## Chapter 12: Fetch Posts for the Feed 🚀

Now that you've mastered creating many-to-many relationships with Django's `ManyToManyField`, it’s time to put that knowledge to work by building a dynamic feed. 

In this chapter, we'll learn how to fetch posts from multiple sources—like blog posts and photos—to create a combined feed that’s relevant to the user. 

### 1. Crafting Complex Queries With Field Lookups 🔍

The first step in building a personalized feed is fetching blog posts from creators that the logged-in user follows. This involves querying models based on relationships, such as finding blog posts contributed by creators the user is following. 

In Django, this can be done using field lookups with double underscores (`__`):

```python
blogs = Blog.objects.filter(contributors__in=request.user.userprofile.following.all())
```

This query retrieves all blog posts where contributors are among the users that the current user follows.

### 2. Filtering Related Data Using `exclude()` and Multiple Conditions 🎛️

To enhance the feed, we need to fetch photos that meet certain criteria. Suppose we want to include photos uploaded by users the current user follows, but that are not already linked to the fetched blogs:

```python
photos = Photo.objects.filter(
    uploader__in=request.user.userprofile.following.all()
).exclude(
    blog__in=blogs
)
```

This approach filters out any photos that belong to the blogs we have already retrieved, ensuring diversity in the feed content.

### 3. Combining Queries With Q Objects for Flexible Logic 🧩

In some scenarios, we may want to include additional conditions. For example, we can use `Q` objects to apply OR logic, such as including `starred` blog posts even if the contributors aren’t being followed:

```python
from django.db.models import Q

blogs = Blog.objects.filter(
    Q(contributors__in=request.user.userprofile.following.all()) | Q(starred=True)
)
```

Using `Q`, we construct more flexible queries by combining conditions with AND, OR, or NOT operators, adapting to complex feed requirements.

### 4. Merging and Sorting QuerySets With Different Model Types 🌀

To present a unified feed that combines both blogs and photos, we need to merge the retrieved data. Since blog and photo QuerySets are of different model types, merging them directly with Django's `order_by()` isn’t possible. 

Instead, we use Python’s built-in `itertools.chain` to join the QuerySets, and then sort the combined list by the date of creation:

```python
from itertools import chain

combined_feed = sorted(
    chain(blogs, photos),
    key=lambda instance: instance.date_created,
    reverse=True
)
```

This approach results in a sorted feed that displays the most recent content first, regardless of whether it's a blog post or a photo.


### Summary ✨

- **Field lookups** help us fetch related data using relationships between models.
- **Q objects** allow us to add flexibility to our queries with logical operators.
- **Combining QuerySets** with `itertools.chain` and sorting enables us to build unified and dynamic feeds.

This chapter has shown you how to fetch and combine different types of content for a personalized feed, setting the stage for more advanced user experiences in your Django application! 🎉

---