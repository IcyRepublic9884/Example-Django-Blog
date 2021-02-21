# Example-Django-Blog
A simple Blog made with Django 3.1 and Bootstrap.
Some of the Code is from **Corey Schafer's** <a href="https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g">Django Tutorial</a><br><br>

## Installation and Running
To Run this web application, you should have python installed on you system.
if not go to <a href="https://www.python.org">python.org</a> and download and install it.

After installing python, open up a terminal and type<br><br>
<code>$ python3 -m pip install django django-crispy-forms</code><br>
<small>For windows, replace <code>python3</code> with <code>py -3</code></small>

after the installation, go to the project home, open up a terminal, (or cmd for windows) and type<br>

<code>$ python manage.py runserver</code>

Now open up a browser and go to <code>localhost port 8000</code><br>
<a herf="https://localhost:8000">127.0.0.1:8000</a>

## Acessing The Admin Page
The default admin username and password should be, themiya and 1122.
otherwise, to cerate your own super user, run the following command<br>

<code>$ python manage.py createsuperuser</code><br>

This will prompt you for you creadentials, and add you to the database

## Deleting Database
If you want to start fresh, with our own posts, users and images, delete the following files and foulders,
<ul>
    <li>db.sqlite3</i>
    <li>files in the media directory</li>
</ul>
After the deleting, run the following command in the terminal<br><br>
<code>$ python manage.py migrate</code><br>
<br>
This should re-create the database, but this time it will be empty.
You need to create a new super user to acess the admin page and all the posts, users and data of the web app will be deleted.