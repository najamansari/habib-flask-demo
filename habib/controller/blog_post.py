"""The blog_post controller.

This is where the actual business logic gets defined.
"""

from datetime import datetime
from habib import database


def list_blog_posts():
    """Returns the blog posts from the database.
    """
    return database.Session.query(database.BlogPost).all()


def get_post(post_id):
    """Return a particular blog posts from the database.

    :param post_id: The post ID to look up in the database.
    """
    return database.Session.query(database.BlogPost).filter(database.BlogPost.id == post_id).all()


def add_post(title, post, author):
    """Adds a new blog post to the database.

    :param title: The title of the blog post
    :param post: The post content
    :param author: The author of the blog post
    """
    new_entry = database.BlogPost(
        title=title, post=post, author=author, created_date=datetime.now(),
        modified_date=datetime.now()
    )
    database.Session().add(new_entry)
    database.Session.commit()


def get_random_id():
    """Returns the ID of a single blog post from the database.

    If the database is empty, should result in an error.
    """
    return database.Session.query(database.BlogPost.id).first()[0]


def get_post_by_title_author_and_post(title, post, author):
    """Looks for the given information in the database.

    :param title: The title of the blog post
    :param post: The post content
    :param author: The author of the blog post
    """
    return database.Session.query(database.BlogPost).filter(
        database.BlogPost.title == title
    ).filter(
        database.BlogPost.post == post
    ).filter(
        database.BlogPost.author == author
    ).all()
