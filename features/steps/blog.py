import random
from behave import given, when, then
from habib.controller import blog_post

random.seed()


@given(u'a user visits the {page}')
def step_impl(context, page):
    pass


@when(u'a {verb} request is performed on {uri}')
def step_impl(context, verb, uri):
    if "GET" == verb:
        context.response = context.app.get(uri)
    elif "POST" == verb:
        context.response = context.app.post(uri, data=context.form)


@then(u'the {page} should be returned')
def step_impl(context, page):
    context.response_data = context.response.get_data()


@then(u'the {header} header should be present')
def step_impl(context, header):
    assert header in context.response.headers


@then(u'the {header} header should contain {content_type}')
def step_impl(context, header, content_type):
    assert content_type in context.response.headers.get(header)


# @then(u'the response should be a valid HTML document')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the response should be a valid HTML document')


# @then(u'the body tag should contain table')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the body tag should contain table')


# @then(u'the table tag should contain row')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the table tag should contain row')


# @then(u'all row tags should contain 3 elements')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then all row tags should contain 3 elements')

@then(u'the user gets redirected to /blog')
def step_impl(context):
    return context.app.get('/blog')


@then(u'return new blog post form')
def step_impl(context):
    return context.app.get('/blog/new')


@then(u'the status code should be {status:d}')
def step_impl(context, status):
    assert status == context.response.status_code


@given(u'a user wants to open a blog post that exists')
def step_impl(context):
    context.blog_post_id = blog_post.get_random_id()


@when(u'the user opens the blog post')
def step_impl(context):
    context.response = context.app.get('/blog/%d' % context.blog_post_id)


@given(u'a user wants to open a blog post that does not exist')
def step_impl(context):
    context.blog_post_id = random.randint(-100, 0)


@given(u'the user wants to create a blog post')
def step_impl(context):
    context.form = {}


@given(u'the {keyword} is {value}')
def step_impl(context, keyword, value):
    context.form[keyword] = value


@then(u'the new post should be created in the database')
def step_impl(context):
    assert blog_post.get_post_by_title_author_and_post(
        context.form.get("title"), context.form.get("post"),
        context.form.get("author")
    )
