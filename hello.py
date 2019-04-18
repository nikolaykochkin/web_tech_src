def app(environ, start_response):
    body = environ['QUERY_STRING'].split('&')
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    return body
