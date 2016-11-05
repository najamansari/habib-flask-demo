Feature: Sample Blog
    Tests for our sample blog application

    Scenario: User visits the index page
        Given a user visits the index page
        When a GET request is performed on /blog
        Then the index page should be returned
        And the Content-Type header should be present
        And the Content-Type header should contain text/html
        # And the response should be a valid HTML document
        # And the body tag should contain table
        # And the table tag should contain row
        # And all row tags should contain 3 elements