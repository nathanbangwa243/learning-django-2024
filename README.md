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
