# habib-flask-demo
A small demo application made during a workshop conducted at Habib University, Karachi.

This workshop is the first in a series that aims to introduce students to the development of web applications and the tools and technologies that are currently being used by professionals.

# Running the Application
Assuming you are on a *NIX system, set up a virtualenv and activate it. Typically the following should work just fine:

```bash
virtualenv env
source env/bin/activate
```

Once the virtualenv has loaded, install the dependencies required:

```bash
pip install -r requirements.txt
```

Now you can run the app using:

```bash
python webapp.py
```

By default the application runs on port 5000 and currently we have set it to run in debug mode. This means that in case of any errors, a stack trace and debug prompt will be shown in your browser. You may also use a debugger to connect to the application directly and debug it.
