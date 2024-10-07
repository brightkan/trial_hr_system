import time
from .models import APIRequestLog


class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path starts with /api/
        if request.path.startswith('/api/'):
            # Start time for request
            start_time = time.time()

            # Get the endpoint and HTTP method
            endpoint = request.path
            method = request.method

            # Call the view and get the response
            response = self.get_response(request)

            # Check if the response status code indicates success (2xx status codes)
            success = 200 <= response.status_code < 300

            # Log the API request
            APIRequestLog.objects.create(
                endpoint=endpoint,
                method=method,
                status_code=response.status_code,
                success=success
            )

            # Calculate the duration of the request processing (optional)
            duration = time.time() - start_time
        else:
            # If it's not an API request, just call the view and return the response
            response = self.get_response(request)

        return response
