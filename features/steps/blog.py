from behave import given, when, then


@given(u'a user visits the index page')
def step_impl(context):
    pass


@when(u'a {verb} request is performed on {uri}')
def step_impl(context, verb, uri):
    if "GET" == verb:
        context.response = context.app.get(uri)


@then(u'the index page should be returned')
def step_impl(context):
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
