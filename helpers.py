def format_response(res):
    return res.content, res.status_code, res.headers.items()