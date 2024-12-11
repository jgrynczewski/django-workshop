# https://docs.djangoproject.com/en/5.1/topics/http/middleware/
# function-based approach
def new_middleware(get_response):

    def middleware(request):

        # before processing the view
        print("Before")

        response = get_response(request)

        # after the view has been executed
        print("After")
        return response

    return middleware


# class-based approach
class NewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Before")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("After")

        return response


# + aktywacja: "extras_app.middleware.new_middleware"
# lub "extras_app.middleware.NewMiddleware"
