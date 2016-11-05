from webapp import app


def before_all(context):
    context.app = app.test_client()
