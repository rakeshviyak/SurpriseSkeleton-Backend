## SurpriseSkeleton-Backend
Simple bare backend skeleton


## Setup the Python environment
Make sure you have installed python and pip 

Install virtualenv because it's pretty neat.

<pre>$ sudo aptitude install python-virtualenv</pre>
or
<pre>$ sudo pip install virtualenv</pre>


Now that we have python, virtualenv and pip installed let's set up a directory for our project.
<pre>
$ mkdir todo
$ cd todo
$ virtualenv env
New python executable in env/bin/python
Installing distribute…….[a lot of dots]..done.
$ source env/bin/activate
(env)$
</pre>

Now that we have python, virtualenv and pip installed let's set up a directory for our project.
<pre>
$ mkdir todo
$ cd todo
$ virtualenv env
New python executable in env/bin/python
Installing distribute…….[a lot of dots]..done.
$ source env/bin/activate
(env)$
</pre>

We created a directory, we moved into and then we had virtualenv create a virtual environment for our project. At the very end we activated this virtual environment so we can work within it.  Notice it changed your prompt to include (env).

<pre>
(env)$ pip install -r requirements.txt
</pre>

And some downloading and unpacking you should get:

<pre>
Successfully installed Flask Jinja2 Werkzeug, etc
Cleaning up…
</pre>


## Hello Api usage 

We now have Flask and are ready to start the first bit of our app. 

<pre>
(env)$ python todo.py
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
</pre>

Point your web browser at [http://localhost:5000/api/todo] . To stop your Flask app, press ctrl+c.

-GET
<pre>
http://localhost:5000/api/todo/<id>
*eg.
http://localhost:5000/api/todo/
*List all items in json
http://localhost:5000/api/todo/1
*List item with id:1 in json
http://localhost:5000/api/todo?q={"filters":[{"name":"title","op":"eq","val":"come on bitch"}]}
*using filters
</pre>

-POST
<pre>
http://localhost:5000/api/todo/
*header
Content-type: application:json
*body (in json)
{"title" : "need to add mysql"}
</pre>

[Detailed link on the usgae of api](https://flask-restless.readthedocs.org/)




