Feature: Sample Blog
    Tests for our sample blog application

    Scenario: User visits the index page
        Given a user visits the index page
        When a GET request is performed on /blog
        Then the index page should be returned
        And the Content-Type header should be present
        And the Content-Type header should contain text/html

        # And the body tag should contain table
        # And the table tag should contain row
        # And all row tags should contain 3 elements

    Scenario: User visits the / URL
        Given a user visits the / URL
        When a GET request is performed on /
        Then the user gets redirected to /blog

    Scenario: User visits the /blog/ID
        Given a user visits the /blog/ID
        When a GET request is performed on blogURL
        Then the /blog/ID page should be returned
        #Error if does not exist

    Scenario: User creates a new blog post
        Given a user visits the /blog/new URL
        When a GET request is performed on /blog/new
        Then return new blog post form
        When a POST request is performed on /blog/new
        Then create a new blog post 
