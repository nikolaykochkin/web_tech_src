def app(environ, start_response):	
	data = bytes('\n'.join(environ['QUERY_STRING'].split('&')),encoding = 'utf-8')
	status = '200 OK'
	response_headers = [
		('Content-type', 'text/plain')
	]
	start_response(status, response_headers)
	return [data]
