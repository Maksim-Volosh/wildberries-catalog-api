class NoAccessToWildberriesAPI(Exception):
    """
    Exception raised when access to the Wildberries API is not possible.

    This exception is typically raised when a request to the Wildberries API
    results in an unexpected response, such as a non-200 HTTP status code.

    """

    ...
