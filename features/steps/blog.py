from behave import given, when, then


@given(u'a user visits the {uri}')
def step_impl(context):
    pass


@when(u'a {verb} request is performed on {uri}')
def step_impl(context, verb, uri):
    if "GET" == verb:
        context.response = context.app.get(uri)
#    if "POST" == verb: ##Maybe?
 #   	context.app.create(uri)


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

@then(u'the user gets redirected to /blog')
def step_impl(context):
    return context.app.get('/blog')


@then(u'the /blog/{ID} should be returned')
def step_impl(context,id):
    if context.app.get('/blog/'+str(id)): #exists#:
    	return context.app.get('/blog/id')
    else:
    	raise AssertionError
@then(u'return new blog post form')
def step_impl(context):
    return context.app.get('/blog/new')

@then(u'create a new blog post')
def step_impl(context):
    #Dont know how to do this.##raise NotImplementedError(u'STEP: Then create a new blog post')
    pass
