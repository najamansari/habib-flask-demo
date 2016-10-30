"""Views for the app.
"""

from flask import Flask, render_template, request, url_for, redirect
from webapp import app
from habib.controller import blog_post


@app.route("/")
def redirect_to_blog():
    """Returns an HTTP redirect to our blog lists page.

    If you open this URI in your browser (i.e. http://localhost:5000/), you will
    be automatically redirected to the blog post list page. In order to
    visualize what's going on, here's the output from cURL:
        curl -v http://localhost:5000/
        *   Trying 127.0.0.1...
        * Connected to localhost (127.0.0.1) port 5000 (#0)
        > GET / HTTP/1.1
        > Host: localhost:5000
        > User-Agent: curl/7.47.0
        > Accept: */*
        >
        * HTTP 1.0, assume close after body
        < HTTP/1.0 302 FOUND
        < Content-Type: text/html; charset=utf-8
        < Content-Length: 217
        < Location: http://localhost:5000/blog
        < Server: Werkzeug/0.11.11 Python/2.7.12
        < Date: Sat, 29 Oct 2016 18:02:45 GMT
        <
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>Redirecting...</title>
        <h1>Redirecting...</h1>
        * Closing connection 0
        <p>You should be redirected automatically to target URL: <a href="/blog">/blog</a>.  If not click the link.

    You can read more about HTTP redirection at:
    http://stackoverflow.com/questions/973098/what-does-http-1-1-302-mean-exactly
    https://en.wikipedia.org/wiki/URL_redirection#HTTP_status_codes_3xx
    """
    return redirect(url_for("return_blogs_list"))


@app.route("/blog")
def return_blogs_list():
    """Return the blog posts list.

    Uses the Flask render_template function to render the index page and return
    it to the user.
    """
    return render_template("index.html", blog_posts=blog_post.list_blog_posts())


@app.route("/blog/<post_id>")
def return_blog_post(post_id):
    """Return a particular post.

    Uses the Flask render_template function to render the index page and return
    it to the user.
    """
    return render_template("blog.html", blog_post=blog_post.get_post(post_id))


@app.route("/blog/new", methods=["GET", "POST"])
def new_post():
    """Handles post creation.

    Checks the request method, if the user performed a GET request, returns the
    new post form. Adds the entry to the database and returns the user to the
    form if a POST request was performed. Any other request methods will be
    rejected.
    """
    if "GET" == request.method:
        return render_template("add_new.html")
    blog_post.add_post(request.form.get("title"), request.form.get("post"),
                       request.form.get("author"))
    return redirect(url_for("new_post"))
