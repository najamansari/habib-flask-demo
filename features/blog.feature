Feature: Sample Blog
    Tests for our sample blog application

    Scenario: User visits the index page
        Given a user visits the index page
        When a GET request is performed on /blog
        Then the index page should be returned
        And the Content-Type header should be present
        And the Content-Type header should contain text/html
        And the status code should be 200

        # And the body tag should contain table
        # And the table tag should contain row
        # And all row tags should contain 3 elements

    Scenario: User visits the / URL
        Given a user visits the root URL
        When a GET request is performed on /
        Then the Location header should be present
        And the Location header should contain /blog
        And the status code should be 302

    Scenario: User opens a blog post that exists
        Given a user wants to open a blog post that exists
        When the user opens the blog post
        Then the blog post should be returned
        And the Content-Type header should be present
        And the Content-Type header should contain text/html
        And the status code should be 200

    Scenario: User opens a blog post that does not exist
        Given a user wants to open a blog post that does not exist
        When the user opens the blog post
        Then the error page should be returned
        And the Content-Type header should be present
        And the Content-Type header should contain text/html
        And the status code should be 200

    Scenario: User visits the new blog page
        Given a user visits the /blog/new URL
        When a GET request is performed on /blog/new
        Then the new blog post form should be returned
        And the Content-Type header should be present
        And the Content-Type header should contain text/html
        And the status code should be 200

    Scenario: User creates a new blog post
        Given the user wants to create a blog post
        And the title is Post made during test run
        And the post is A test post
        And the author is The Test Runner
        When a POST request is performed on /blog/new
        Then the new post should be created in the database
        And the Location header should be present
        And the Location header should contain /blog/new
        And the status code should be 302
