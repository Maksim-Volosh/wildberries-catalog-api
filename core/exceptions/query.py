class QueryIsRequired(Exception):
    """Exception raised when a query parameter is required but not provided."""

    ...
    
class NotFoundByQuery(Exception):
    """Exception raised when no products were found by query parameter."""
    ...