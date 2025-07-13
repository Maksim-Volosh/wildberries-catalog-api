from urllib.parse import parse_qsl

def extract_allowed_filters(request) -> dict:
    """
    Extracts allowed filters from the request's query parameters.

    This function retrieves query parameters from the request and filters them
    based on a predefined set of allowed filters. The resulting dictionary contains
    only those query parameters whose keys match the allowed filters.

    Args:
        request: The HTTP request object containing query parameters.

    Returns:
        A dictionary of filtered query parameters that are allowed for further processing.
    """

    allowed_filters = {
        "min_price", "max_price",
        "min_rating", "max_rating",
        "min_feedbacks", "max_feedbacks", "name"
    }
    
    query_params = dict(parse_qsl(request.META.get('QUERY_STRING', '')))
    
    filtered_params = {k: v for k, v in query_params.items() if k in allowed_filters}
    
    return filtered_params