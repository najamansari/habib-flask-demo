"""The web app module.

This is the main entry-point of our application. Here we create our Flask
 object and import all our views. Please note that the views have to be
 imported _after_ creating the Flask object. Even though this violates at least
 two Python best-practices.
 1) Keeping imports at the top of your modules
 2) Not leaving behind any unused imports.
 In this case, it is a necessary evil.
"""

from flask import Flask

app = Flask(__name__)

from habib.views import *

if "__main__" == __name__:
    app.run(debug=True)
