import hashlib

def build_cache_key(filtered_params: dict) -> str:
    if not filtered_params:
        return "products:base"
    
    params_string = "&".join(f"{k}={filtered_params[k]}" for k in sorted(filtered_params))
    
    hashed = hashlib.md5(params_string.encode()).hexdigest()
    
    return f"products:{hashed}"