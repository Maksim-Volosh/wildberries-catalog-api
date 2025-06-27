import hashlib
from urllib.parse import parse_qsl

def make_cache_key(request):
    allowed_filters = {
        "min_price", "max_price",
        "min_rating", "max_rating",
        "min_feedbacks", "max_feedbacks", "name"
    }
    
    query_params = dict(parse_qsl(request.META.get('QUERY_STRING', '')))
    
    filtered_params = {k: v for k, v in query_params.items() if k in allowed_filters}
    
    if not filtered_params:
        return "products:base"
    
    params_string = "&".join(f"{k}={filtered_params[k]}" for k in sorted(filtered_params))
    
    hashed = hashlib.md5(params_string.encode()).hexdigest()
    
    return f"products:{hashed}"